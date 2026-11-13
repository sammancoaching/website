# Sanity check for assets/js/hubspot_form_theme.js: every colour token it copies
# into the HubSpot form must be defined in _sass/_tokens.scss, for both the
# light theme and the dark one. No browser or server needed.
from pathlib import Path
import re

ROOT = Path(__file__).parent.parent


def test_hubspot_form_theme_uses_only_defined_tokens():
    js = (ROOT / 'assets/js/hubspot_form_theme.js').read_text(encoding='utf-8')
    scss = (ROOT / '_sass/_tokens.scss').read_text(encoding='utf-8')
    light, dark = scss.split('@mixin dark-tokens')

    used = re.findall(r": '(--color-[\w-]+)'", js)
    assert used, 'found no tokens in hubspot_form_theme.js'

    for token in used:
        assert f'{token}:' in light, f'{token} is not defined for the light theme'
        assert f'{token}:' in dark, f'{token} is not defined for the dark theme'
