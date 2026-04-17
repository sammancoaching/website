import os
from pathlib import Path

def test_expired_offer_not_visible():
    """Verify that an offer with an expired date is not present on the offers page."""
    
    offers_page_path = Path("_site/offers/index.html")
    assert offers_page_path.exists(), "The offers page was not generated at _site/offers/index.html. Run 'bundle exec jekyll build' first."
    
    # Read the generated HTML
    with open(offers_page_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # This matches the title of _offers/expired_test_offer.md
    expired_title = "THIS OFFER IS EXPIRED AND SHOULD NOT BE VISIBLE"
    assert expired_title not in html_content.upper(), f"The expired offer '{expired_title}' was found in the offers page, but it should be hidden."
