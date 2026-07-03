from pathlib import Path

import yaml


def read_page(relative_path):
    page_path = Path("_site") / relative_path
    assert page_path.exists(), f"{page_path} was not generated. Run 'bundle exec jekyll build' first."
    return page_path.read_text(encoding="utf-8")


def load_coaching_offers():
    with open("_data/coaching_offers.yml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_contributors():
    with open("_data/contributors.yml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def coaches_for(offer_key):
    return {
        key: contributor
        for key, contributor in load_contributors().items()
        if contributor.get("member") and offer_key in contributor.get("offers", [])
    }


def test_offers_index_lists_all_services():
    html = read_page("society/offers/index.html")

    for offer_key, offer in load_coaching_offers().items():
        assert offer["title"].upper() in html.upper(), f"Service '{offer['title']}' missing from offers page."
        assert f'society/offers/{offer["slug"]}.html' in html, f"No link to the {offer_key} detail page."


def test_offers_index_shows_coach_counts():
    html = read_page("society/offers/index.html")

    for offer_key in load_coaching_offers():
        count = len(coaches_for(offer_key))
        plural = "coach offers" if count == 1 else "coaches offer"
        assert f"{count} {plural} this" in html, f"Expected coach count '{count}' for {offer_key}."


def test_detail_pages_list_tagged_member_coaches():
    contributors = load_contributors()

    for offer_key, offer in load_coaching_offers().items():
        html = read_page(f"society/offers/{offer['slug']}.html")

        for key, contributor in contributors.items():
            name = contributor["title"]
            if key in coaches_for(offer_key):
                assert name in html, f"{name} should be listed on the {offer_key} page."
            else:
                # match the coach-row name element to avoid false positives from page prose
                assert f'coach-row__name">{name}<' not in html, \
                    f"{name} should NOT be listed as a coach on the {offer_key} page."


def test_detail_pages_link_back_and_cross_link():
    offers = load_coaching_offers()

    for offer_key, offer in offers.items():
        html = read_page(f"society/offers/{offer['slug']}.html")

        assert "All coaching offers" in html, f"Back link missing on the {offer_key} page."
        for other_key, other in offers.items():
            if other_key != offer_key:
                assert f'society/offers/{other["slug"]}.html' in html, \
                    f"Cross-link to {other_key} missing on the {offer_key} page."
