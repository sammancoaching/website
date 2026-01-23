require 'tzinfo'

module Jekyll
  module TimezoneFilter
    def to_local_time(input)
      return input if input.nil?
      
      site_timezone = @context.registers[:site].config['timezone']
      return input unless site_timezone
      
      begin
        # Parse the input time (preserves timezone info if present)
        input_time = Time.parse(input.to_s)
        
        # Get the target timezone
        target_tz = TZInfo::Timezone.get(site_timezone)
        
        # Convert to UTC first (handles any input timezone), then to target timezone
        utc_time = input_time.getutc
        local_time = target_tz.to_local(utc_time)
        
        local_time
      rescue => e
        Jekyll.logger.warn "Timezone conversion error:", e.message
        input
      end
    end
  end
end

Liquid::Template.register_filter(Jekyll::TimezoneFilter)
