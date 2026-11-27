# Unit tests for _plugins/calendar_events.rb. Each event's front matter sits
# right next to its tests, and "now" is fixed, so they don't depend on the
# site's real event dates or on today's date.
#
#     ruby tests/ruby/calendar_events_test.rb

require 'minitest/autorun'
require 'yaml'
require 'jekyll'
require_relative '../../_plugins/calendar_events'

FakeSite = Struct.new(:config, :pages)
FakeDoc = Struct.new(:data, :basename_without_ext, :relative_path, :url)

module CalendarEventTestHelpers
  NOW = Time.utc(2030, 6, 1, 12, 0)

  def event(front_matter, now: NOW)
    data = YAML.safe_load(front_matter)
    key = data['event_key']
    site = FakeSite.new({ 'url' => 'https://sammancoaching.org', 'timezone' => 'Europe/Stockholm' }, [])
    doc = FakeDoc.new(data, key, "_upcoming_events/#{key}.md", "/society/events/#{key}.html")
    Jekyll::CalendarEvent.new(site, doc, now: now)
  end

  def ics(event)
    # iCalendar folds long lines with CRLF + space
    event.send(:ics_calendar).to_ical.gsub(/\r?\n[ \t]/, '')
  end

  def query(url)
    URI.decode_www_form(URI(url).query).to_h
  end
end

class SingleDateTest < Minitest::Test
  include CalendarEventTestHelpers

  # One-off events use a one-item `dates` list, like the site's own events.
  OPEN_SPACE = <<~YAML
    event_key: open_space
    calendar_title: Samman Society Open Space
    dates:
      - "2030-07-10 16:00"
    duration_minutes: 60
    timezone: Europe/Berlin
    location: Online
  YAML

  def test_next_date_is_the_start
    data = event(OPEN_SPACE).liquid_data
    assert data['has_upcoming_date']
    assert_equal Time.utc(2030, 7, 10, 14, 0), data['next_start_utc']
    assert_equal Time.utc(2030, 7, 10, 15, 0), data['next_end_utc']
  end

  def test_google_link_converts_berlin_summer_time_to_utc
    google = event(OPEN_SPACE).liquid_data['calendar_links']['google']
    assert_equal '20300710T140000Z/20300710T150000Z', query(google)['dates']
  end

  def test_google_link_converts_berlin_winter_time_to_utc
    winter = OPEN_SPACE.sub('2030-07-10', '2030-12-11')
    google = event(winter).liquid_data['calendar_links']['google']
    assert_equal '20301211T150000Z/20301211T160000Z', query(google)['dates']
  end

  def test_ics_has_one_event_with_a_stable_uid
    cal = ics(event(OPEN_SPACE))
    assert_equal 1, cal.scan('BEGIN:VEVENT').size
    assert_includes cal, 'UID:open_space@sammancoaching.org'
    assert_includes cal, 'DTSTART;TZID=Europe/Berlin:20300710T160000'
    assert_includes cal, 'DTEND;TZID=Europe/Berlin:20300710T170000'
    assert_includes cal, 'TRIGGER:-PT30M'
  end

  def test_past_start_has_no_upcoming_date_and_an_empty_calendar
    past = event(OPEN_SPACE, now: Time.utc(2030, 8, 1))
    refute past.liquid_data['has_upcoming_date']
    assert_empty past.liquid_data['calendar_links']
    refute_includes ics(past), 'BEGIN:VEVENT'
  end
end

class DatesListTest < Minitest::Test
  include CalendarEventTestHelpers

  # Deliberately out of order, and the May date is before NOW.
  LEARNING_HOUR = <<~YAML
    event_key: learning_hour
    calendar_title: Samman Learning Hour
    dates:
      - "2030-12-04 17:00"
      - "2030-05-15 17:00"
      - "2030-09-18 17:00"
    duration_minutes: 90
    timezone: Europe/Berlin
  YAML

  def test_upcoming_dates_are_sorted_and_past_dates_dropped
    dates = event(LEARNING_HOUR).liquid_data['upcoming_dates']
    assert_equal [Time.utc(2030, 9, 18, 15, 0), Time.utc(2030, 12, 4, 16, 0)], dates.map { |d| d['start_utc'] }
  end

  def test_next_date_is_the_first_upcoming_one
    assert_equal Time.utc(2030, 9, 18, 15, 0), event(LEARNING_HOUR).liquid_data['next_start_utc']
  end

  def test_no_upcoming_date_when_all_dates_are_past
    data = event(LEARNING_HOUR, now: Time.utc(2031, 1, 1)).liquid_data
    refute data['has_upcoming_date']
    assert_empty data['upcoming_dates']
  end

  def test_each_date_has_calendar_links_for_its_own_date
    googles = event(LEARNING_HOUR).liquid_data['upcoming_dates'].map { |d| query(d['calendar_links']['google'])['dates'] }
    assert_equal ['20300918T150000Z/20300918T163000Z', '20301204T160000Z/20301204T173000Z'], googles
  end

  def test_ics_has_one_event_per_upcoming_date_with_distinct_uids
    cal = ics(event(LEARNING_HOUR))
    assert_equal 2, cal.scan('BEGIN:VEVENT').size
    assert_includes cal, 'UID:learning_hour-20300918@sammancoaching.org'
    assert_includes cal, 'UID:learning_hour-20301204@sammancoaching.org'
    refute_includes cal, '20300515'
  end
end

class RepeatingEventTest < Minitest::Test
  include CalendarEventTestHelpers

  # Fridays from 3 May 2030; NOW (1 June) is part-way through the series.
  ENSEMBLE = <<~YAML
    event_key: ensemble
    calendar_title: Samman Society Ensemble
    start: "2030-05-03 15:00"
    duration_minutes: 60
    timezone: Europe/Berlin
    rrule: FREQ=WEEKLY;COUNT=23;INTERVAL=1;BYDAY=FR
  YAML

  def test_next_date_is_the_next_repeat
    assert_equal Time.utc(2030, 6, 7, 13, 0), event(ENSEMBLE).liquid_data['next_start_utc']
  end

  def test_ics_exports_the_series_from_its_first_date
    cal = ics(event(ENSEMBLE))
    assert_equal 1, cal.scan('BEGIN:VEVENT').size
    assert_includes cal, 'DTSTART;TZID=Europe/Berlin:20300503T150000'
    assert_includes cal, 'RRULE:FREQ=WEEKLY;COUNT=23;INTERVAL=1;BYDAY=FR'
  end

  def test_google_link_carries_the_repeat_rule_from_the_first_date
    google = query(event(ENSEMBLE).liquid_data['calendar_links']['google'])
    assert_equal 'RRULE:FREQ=WEEKLY;COUNT=23;INTERVAL=1;BYDAY=FR', google['recur']
    assert_equal '20300503T130000Z/20300503T140000Z', google['dates']
  end

  def test_outlook_and_yahoo_fall_back_to_the_ics_file
    links = event(ENSEMBLE).liquid_data['calendar_links']
    %w[outlook_com office365 yahoo].each { |name| assert_equal '/society/events/ensemble.ics', links[name] }
  end

  def test_no_upcoming_dates_list
    refute event(ENSEMBLE).liquid_data.key?('upcoming_dates')
  end
end

class FrontMatterErrorsTest < Minitest::Test
  include CalendarEventTestHelpers

  def test_start_and_dates_together
    error = assert_raises(ArgumentError) { event(<<~YAML) }
      event_key: broken
      timezone: Europe/Berlin
      start: "2030-07-10 16:00"
      dates: ["2030-07-10 16:00"]
    YAML
    assert_match 'either `start` or `dates`', error.message
  end

  def test_dates_with_rrule
    error = assert_raises(ArgumentError) { event(<<~YAML) }
      event_key: broken
      timezone: Europe/Berlin
      dates: ["2030-07-10 16:00"]
      rrule: FREQ=WEEKLY;COUNT=3
    YAML
    assert_match '`rrule` only works with `start`', error.message
  end

  def test_empty_dates
    error = assert_raises(ArgumentError) { event(<<~YAML) }
      event_key: broken
      timezone: Europe/Berlin
      dates: []
    YAML
    assert_match '`dates` must be a non-empty list', error.message
    assert_match '_upcoming_events/broken.md', error.message
  end
end
