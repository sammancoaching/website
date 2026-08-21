import re
from pathlib import Path

import yaml

# Mirrors the pattern in _plugins/connects_index_generator.rb - kept as a
# separate implementation so this test independently verifies the plugin's
# behaviour rather than restating it.
CONNECT_LINK_PATTERN = re.compile(r"_activities/connect/([a-zA-Z0-9_\-]+)\.md")


def _learning_hour_source_files():
    return sorted(Path("_learning_hours").rglob("*.md"))


def _front_matter_title(path):
    text = path.read_text(encoding="utf-8")
    front_matter = text.split("---", 2)[1]
    return yaml.safe_load(front_matter)["title"]


def _generated_url(path):
    relative = path.relative_to("_learning_hours")
    return "/learning_hours/" + relative.with_suffix(".html").as_posix()


def _expected_learning_hours_for(connect_slug):
    expected = []
    for path in _learning_hour_source_files():
        slugs = CONNECT_LINK_PATTERN.findall(path.read_text(encoding="utf-8"))
        if connect_slug in slugs:
            expected.append((_front_matter_title(path), _generated_url(path)))
    return sorted(expected)


def _connect_activity_slugs():
    return sorted(p.stem for p in Path("_activities/connect").glob("*.md"))


def test_connect_activity_pages_list_learning_hours_that_use_them():
    for slug in _connect_activity_slugs():
        page_path = Path("_site/activities/connect") / f"{slug}.html"
        assert page_path.exists(), f"{page_path} was not generated. Run 'bundle exec jekyll build' first."
        html = page_path.read_text(encoding="utf-8")

        expected = _expected_learning_hours_for(slug)
        if not expected:
            assert "Used in these Learning Hours" not in html, (
                f"{slug} page shows a 'Used in these Learning Hours' section but no learning hour links to it."
            )
            continue

        assert "Used in these Learning Hours" in html, f"{slug} page is missing its 'Used in these Learning Hours' section."
        for title, url in expected:
            assert url in html, f"{slug} page is missing a link to {url}."
            assert title in html, f"{slug} page is missing the title '{title}'."
