require 'erb'
require 'icalendar'
require 'icalendar/tzinfo'
require 'ice_cube'
require 'tzinfo'

module Jekyll
  # For each upcoming event with a `start` in its front matter: work out the
  # next date that hasn't ended yet, expose it (and "add to calendar" links)
  # to Liquid, and write /society/events/<key>.ics for download or subscription.
  class CalendarEventsGenerator < Generator
    safe true
    priority :normal

    def generate(site)
      collection = site.collections['upcoming_events']
      return unless collection

      collection.docs.each do |doc|
        next unless doc.data['start']

        event = CalendarEvent.new(site, doc)
        doc.data.merge!(event.liquid_data)
        site.pages << event.ics_page
      end
    end
  end

  class CalendarEvent
    def initialize(site, doc)
      @site = site
      @doc = doc
      @key = doc.data['event_key'] || doc.basename_without_ext
      @tz = TZInfo::Timezone.get(doc.data['timezone'] || site.config['timezone'])
      @duration = Integer(doc.data['duration_minutes'] || 60) * 60
      @rrule = doc.data['rrule']
      @wall_start = parse_wall_clock(doc.data['start'])
      @next_wall_start = next_wall_start(Time.now.utc)
    end

    def liquid_data
      data = {
        'has_upcoming_date' => !@next_wall_start.nil?,
        'ics_url' => ics_path,
        'event_timezone' => @tz.identifier,
        'calendar_links' => {}
      }
      return data unless @next_wall_start

      start_utc = to_utc(@next_wall_start)
      end_utc = to_utc(@next_wall_start + @duration)
      data.merge(
        'next_start' => @tz.to_local(start_utc),
        'next_end' => @tz.to_local(end_utc),
        'next_start_utc' => start_utc,
        'next_end_utc' => end_utc,
        'calendar_links' => calendar_links(start_utc, end_utc)
      )
    end

    def ics_page
      page = PageWithoutAFile.new(@site, @site.source, 'society/events', File.basename(ics_path))
      page.content = ics_calendar.to_ical
      page.data['layout'] = nil
      page.data['sitemap'] = false
      page
    end

    private

    # `start` is a wall-clock time in the event's timezone. YAML may already
    # have turned it into a Time (in the machine's zone), so read its fields
    # rather than converting it.
    def parse_wall_clock(value)
      t = value.is_a?(String) ? Time.strptime(value.strip, '%Y-%m-%d %H:%M') : value
      Time.utc(t.year, t.month, t.day, t.hour, t.min)
    end

    # Wall-clock times are kept as naive UTC Times so that repeat rules step
    # through local dates (e.g. "every Friday 15:00") across daylight saving.
    def next_wall_start(now_utc)
      schedule = IceCube::Schedule.new(@wall_start)
      schedule.add_recurrence_rule(IceCube::Rule.from_ical(@rrule)) if @rrule
      wall_now = naive(@tz.to_local(now_utc))
      schedule.next_occurrence(wall_now - @duration)
    end

    def naive(local)
      Time.utc(local.year, local.month, local.day, local.hour, local.min, local.sec)
    end

    def to_utc(wall)
      @tz.local_to_utc(wall)
    end

    # Named like the event page, which Jekyll slugifies (open_space -> open-space)
    def ics_path
      "/society/events/#{@key.tr('_', '-')}.ics"
    end

    def site_host
      @site.config['url'].to_s.sub(%r{\Ahttps?://}, '')
    end

    def event_url
      "#{@site.config['url']}#{@doc.url}"
    end

    # The details page holds the sign-up form, so the calendar entry links there.
    def details_url
      details = @site.pages.find { |p| p.relative_path == @doc.data['details_link'] }
      details ? "#{@site.config['url']}#{details.url}" : event_url
    end

    def title
      @doc.data['calendar_title'] || @doc.data['title']
    end

    def description
      [@doc.data['calendar_description'].to_s.strip, details_url].reject(&:empty?).join("\n\n")
    end

    def location
      @doc.data['location'].to_s
    end

    def utc_stamp(time)
      time.utc.strftime('%Y%m%dT%H%M%SZ')
    end

    def calendar_links(start_utc, end_utc)
      q = ->(s) { ERB::Util.url_encode(s) }
      outlook = lambda do |host|
        "https://#{host}/calendar/0/deeplink/compose?path=/calendar/action/compose&rru=addevent" \
          "&subject=#{q[title]}&startdt=#{q[start_utc.utc.iso8601]}&enddt=#{q[end_utc.utc.iso8601]}" \
          "&body=#{q[description]}&location=#{q[location]}"
      end
      google = "https://calendar.google.com/calendar/render?action=TEMPLATE&text=#{q[title]}" \
               "&dates=#{utc_stamp(start_utc)}/#{utc_stamp(end_utc)}" \
               "&details=#{q[description]}&location=#{q[location]}"
      google += "&recur=#{q["RRULE:#{@rrule}"]}" if @rrule

      # Outlook.com, Office 365 and Yahoo can't carry a repeat rule, so
      # repeating events fall back to the .ics download for those.
      return { 'google' => google, 'outlook_com' => ics_path, 'office365' => ics_path, 'yahoo' => ics_path } if @rrule

      {
        'google' => google,
        'outlook_com' => outlook['outlook.live.com'],
        'office365' => outlook['outlook.office.com'],
        'yahoo' => "https://calendar.yahoo.com/?v=60&title=#{q[title]}&st=#{utc_stamp(start_utc)}" \
                   "&et=#{utc_stamp(end_utc)}&desc=#{q[description]}&in_loc=#{q[location]}"
      }
    end

    def ics_calendar
      cal = Icalendar::Calendar.new
      cal.prodid = '-//sammancoaching.org//calendar_events//EN'
      cal.append_custom_property('X-WR-CALNAME', title)
      cal.append_custom_property('REFRESH-INTERVAL;VALUE=DURATION', 'PT12H')
      cal.append_custom_property('X-PUBLISHED-TTL', 'PT12H')
      # No upcoming date: an empty calendar, so subscribers' feeds stay valid.
      return cal unless @next_wall_start

      start_utc = to_utc(@next_wall_start)
      cal.add_timezone(@tz.ical_timezone(start_utc))
      tzid = @tz.identifier
      cal.event do |e|
        e.uid = "#{@key}@#{site_host}"
        e.dtstamp = Icalendar::Values::DateTime.new(Time.now.utc, 'tzid' => 'UTC')
        e.sequence = start_utc.to_i
        e.dtstart = Icalendar::Values::DateTime.new(@next_wall_start, 'tzid' => tzid)
        e.dtend = Icalendar::Values::DateTime.new(@next_wall_start + @duration, 'tzid' => tzid)
        e.summary = title
        e.description = description
        e.location = location unless location.empty?
        e.url = event_url
        e.rrule = @rrule if @rrule
        e.alarm do |a|
          a.action = 'DISPLAY'
          a.description = title
          a.trigger = '-PT30M'
        end
      end
      cal
    end
  end
end
