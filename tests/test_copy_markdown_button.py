# Checks the "Copy as markdown" buttons on the RPG Combat kata page: the
# markdown embedded for each button must be a verbatim slice of the kata source.
from pathlib import Path
import re

import pytest

SOURCE = Path('_kata_descriptions/rpg_combat.md')
BUILT_PAGE = Path('_site/kata_descriptions/rpg_combat.html')


@pytest.fixture(scope="module")
def embedded_markdown():
    html = BUILT_PAGE.read_text(encoding='utf-8')
    blocks = re.findall(
        r'<div class="copy-markdown">.*?'
        r'<button type="button" class="copy-markdown-button" aria-label="Copy as markdown">.*?</button>.*?'
        r'<script type="text/plain" class="copy-markdown-source">(.*?)</script>',
        html, flags=re.DOTALL)
    assert len(blocks) == 2, "expected one button for the original and one for the updated requirements"
    return blocks


def source_between(start_marker, end_marker):
    text = SOURCE.read_text(encoding='utf-8')
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    return text[start:end].strip()


def test_original_requirements_button_copies_the_five_original_sections(embedded_markdown):
    expected = '# RPG Combat\n\n' + source_between('## Damage and Health', '{% endcapture %}')
    assert embedded_markdown[0] == expected
    assert expected.count('\n## ') == 5  # Damage and Health, Levels, Factions, Magical objects, Changing level


def test_updated_requirements_button_copies_the_updated_section(embedded_markdown):
    expected = '# RPG Combat\n\n' + source_between('### Damage and Health', '{% endcapture %}')
    assert embedded_markdown[1] == expected
    assert expected.endswith('they can then also gain additional levels they are entitled to.')


def test_embedded_markdown_is_plain_markdown(embedded_markdown):
    for markdown in embedded_markdown:
        assert '{%' not in markdown
        assert '<' not in markdown


def test_page_content_still_renders_once():
    html = BUILT_PAGE.read_text(encoding='utf-8')
    assert html.count('<h2 id="damage-and-health">') == 1
    assert html.count('<h2 id="updated-requirements">') == 1
    assert html.count('<script src="/assets/js/copy_markdown.js"></script>') == 1


def test_martian_message_button_copies_the_task_description():
    html = Path('_site/kata_descriptions/martian_message.html').read_text(encoding='utf-8')
    blocks = re.findall(r'<script type="text/plain" class="copy-markdown-source">(.*?)</script>', html, flags=re.DOTALL)
    assert len(blocks) == 1
    source = Path('_kata_descriptions/martian_message.md').read_text(encoding='utf-8')
    start = source.index('In the film')
    end = source.index('{% endcapture %}')
    assert blocks[0] == '# Martian Message\n\n' + source[start:end].strip()
    assert 'Quote from the movie' in blocks[0]
