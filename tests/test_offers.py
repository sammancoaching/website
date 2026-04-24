import os
import datetime
import re
from pathlib import Path

def test_expired_offer_not_visible():
    """Verify that an offer with an expired date is not present on the offers page."""
    
    offers_page_path = Path("_site/society/offers/index.html")
    assert offers_page_path.exists(), "The offers page was not generated at _site/offers/index.html. Run 'bundle exec jekyll build' first."
    
    # Read the generated HTML
    with open(offers_page_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # This matches the title of _offers/expired_test_offer.md
    expired_title = "THIS OFFER IS EXPIRED AND SHOULD NOT BE VISIBLE"
    assert expired_title not in html_content.upper(), f"The expired offer '{expired_title}' was found in the offers page, but it should be hidden."


def test_offers_sorted_by_expiry():
    """Verify that offers on the offers page are sorted by expiry date."""

    offers_page_path = Path("_site/society/offers/index.html")
    assert offers_page_path.exists(), "The offers page was not generated at _site/society/offers/index.html."

    with open(offers_page_path, 'r', encoding='utf-8') as f:
        html_content = f.read().upper()

    # Discover offers from the source files
    offers_dir = Path("_offers")
    active_offers = []
    current_date = datetime.date.today().strftime("%Y-%m-%d")

    for offer_file in offers_dir.glob("*.md"):
        with open(offer_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Split front matter
            parts = content.split('---')
            if len(parts) >= 3:
                front_matter_raw = parts[1]
                
                # Simple regex-based front matter parsing since PyYAML is not available
                expiry_date_match = re.search(r'^expiry_date:\s*(.*)$', front_matter_raw, re.MULTILINE)
                title_match = re.search(r'^title:\s*(.*)$', front_matter_raw, re.MULTILINE)
                
                if expiry_date_match and title_match:
                    expiry_date = expiry_date_match.group(1).strip()
                    title = title_match.group(1).strip().upper()
                    
                    if expiry_date >= current_date:
                        active_offers.append({
                            'title': title,
                            'expiry_date': expiry_date
                        })

    # Sort active offers by expiry_date (matching Jekyll's sort: 'expiry_date')
    active_offers.sort(key=lambda x: x['expiry_date'])
    expected_titles = [offer['title'] for offer in active_offers]

    # Find the indices of each title in the HTML
    indices = [html_content.find(title) for title in expected_titles]

    # Check if all titles are found
    missing_titles = [title for title, index in zip(expected_titles, indices) if index == -1]
    assert not missing_titles, f"The following active offers were not found in the page: {missing_titles}"

    # Check if they are in the correct order
    assert indices == sorted(indices), f"Offers are not sorted correctly by expiry_date. Expected order: {expected_titles}. Found indices: {list(zip(expected_titles, indices))}"
