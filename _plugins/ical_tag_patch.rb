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
        ""
      end
    end
  end
end
