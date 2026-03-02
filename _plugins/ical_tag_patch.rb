require 'jekyll-ical-tag'
require 'api_cache'

module Jekyll
  class IcalTag
    class CalendarFetcher
      alias_method :original_fetch, :fetch

      def fetch
        original_fetch
      rescue StandardError => e
        Jekyll.logger.warn "IcalTag:", "Failed to fetch from #{url}: #{e.message}"
        # Return an empty string or some basic valid ICS if possible to avoid further errors in parser
        # but the parser expects a valid ICS to not crash. 
        # Actually Icalendar::Event.parse("") returns [] so it should be safe.
        ""
      end
    end
  end
end
