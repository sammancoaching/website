require 'tzinfo'

module Jekyll
  module TimezoneFilter
    def to_local_time(input)
      return input if input.nil?
      
      site_timezone = @context.registers[:site].config['timezone']
      return input unless site_timezone
      
      begin
        time = Time.parse(input.to_s)
        
        # If the time already has the correct timezone offset, return as-is
        tz = TZInfo::Timezone.get(site_timezone)
        expected_offset = tz.period_for_utc(time.utc).utc_total_offset
        
        if time.utc_offset == expected_offset
          time
        else
          # Convert from UTC to local timezone
          tz.to_local(time.utc)
        end
      rescue => e
        Jekyll.logger.warn "Timezone conversion error:", e.message
        input
      end
    end
  end
end

Liquid::Template.register_filter(Jekyll::TimezoneFilter)
