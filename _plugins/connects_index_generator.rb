module Jekyll
  # Scans each learning hour's raw content for links to connect activities
  # (e.g. "{% link _activities/connect/three_facts.md %}") and records the
  # referenced connect slugs on the document, so a connect activity page can
  # list the learning hours that use it without either page hand-maintaining
  # the relationship.
  class ConnectsIndexGenerator < Generator
    safe true
    priority :low

    CONNECT_LINK_PATTERN = %r{_activities/connect/([a-zA-Z0-9_\-]+)\.md}.freeze

    def generate(site)
      learning_hours = site.collections["learning_hours"]&.docs || []

      learning_hours.each do |doc|
        doc.data["connects"] = doc.content.scan(CONNECT_LINK_PATTERN).flatten.uniq
      end
    end
  end
end
