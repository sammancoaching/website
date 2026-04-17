import os
import re
from pathlib import Path
from datetime import datetime

def test_upcoming_events():
    """
    Checks that:
    * all events are in the future
    * no errors on page
    * all links are valid
    """
    
    events_page_path = Path("_site/society/events/upcoming_events.html")
    assert events_page_path.exists(), "The upcoming events page was not generated at _site/society/events/upcoming_events.html. Run 'bundle exec jekyll build' first."
    
    with open(events_page_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # 1. No errors on page
    # Common Liquid/Jekyll error patterns
    error_indicators = ["Liquid error", "404 Not Found", "Internal Server Error", "exception:"]
    for indicator in error_indicators:
        assert indicator not in html_content, f"Found error indicator '{indicator}' on the upcoming events page."

    # 2. All events are in the future
    # Using regex to extract date components from event-date-block
    # Example:
    # <div class="day">21</div>
    # <div class="month-year">April 2026</div>
    
    # Combined regex to find day and month-year
    # We'll search for pairs of day and month-year
    date_pattern = re.compile(r'<div class="day">(\d+)</div>\s*<div class="month-year">([^<]+)</div>', re.DOTALL)
    matches = date_pattern.findall(html_content)
    
    assert len(matches) > 0, "No upcoming events found on the page. Check if the generation is working correctly."
    
    current_date = datetime(2026, 4, 17) # Specified in issue description: 2026-04-17 14:45
    
    for day_str, month_year_str in matches:
        # month_year_str looks like "April 2026"
        date_str = f"{day_str} {month_year_str}"
        event_date = datetime.strptime(date_str, "%d %B %Y")
        
        assert event_date >= current_date, f"Event on {date_str} is in the past (Current date: {current_date.date()})."

    # 3. All links are valid
    # Find all href="..."
    href_pattern = re.compile(r'href="([^"]+)"')
    links = href_pattern.findall(html_content)
    
    site_root = Path("_site")
    
    for link in links:
        # Ignore external links (starting with http or https)
        if link.startswith("http"):
            continue
            
        # Ignore fragments
        if link.startswith("#"):
            continue

        # Ignore template placeholders (e.g., from search script)
        if "{url}" in link:
            continue
            
        # Remove query parameters/fragments if any
        clean_link = link.split('?')[0].split('#')[0]
        
        if not clean_link:
            continue
            
        # Handle absolute paths relative to site root
        if clean_link.startswith("/"):
            file_path = site_root / clean_link.lstrip("/")
        else:
            # Relative paths
            file_path = events_page_path.parent / clean_link
            
        # If it's a directory, look for index.html
        if file_path.is_dir():
            file_path = file_path / "index.html"
        
        # In some cases Jekyll links to .md as .html or just the directory
        # If the file doesn't exist, try appending .html if it doesn't have it
        if not file_path.exists() and not file_path.name.endswith(".html"):
             if (file_path.with_suffix(".html")).exists():
                 file_path = file_path.with_suffix(".html")

        assert file_path.exists(), f"Broken link found: '{link}' (points to {file_path})."
