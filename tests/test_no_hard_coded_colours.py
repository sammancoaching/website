# Colours are defined once, in _sass/_tokens.scss; every other Sass file uses
# var(--color-*). This fails on a hex, rgb()/hsl() or named colour, or an old
# $brand Sass variable, anywhere else.
# See _docs/design_system.html.
from pathlib import Path
import re

ROOT = Path(__file__).parent.parent

NAMED = r'white|black|red|green|blue|gray|grey|silver|yellow|orange|pink|purple|navy|maroon'
BRAND_VARIABLES = r'\$(coral|dark-blue|off-white|light-blue|light-brown|primary-color)\b'
COLOUR = re.compile(rf'#[0-9a-fA-F]{{3,8}}\b|\b(rgba?|hsla?)\(|:[^;]*\b({NAMED})\b|{BRAND_VARIABLES}')


def test_no_hard_coded_colours_outside_tokens():
    offenders = []
    for scss in sorted((ROOT / '_sass').glob('*.scss')):
        if scss.name == '_tokens.scss':
            continue
        for number, line in enumerate(scss.read_text(encoding='utf-8').splitlines(), 1):
            code = line.split('//')[0]
            if COLOUR.search(code):
                offenders.append(f'{scss.name}:{number}: {line.strip()}')
    assert not offenders, 'Use a token from _tokens.scss instead:\n' + '\n'.join(offenders)
