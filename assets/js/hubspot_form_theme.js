document.addEventListener('DOMContentLoaded', () => {
    // HubSpot forms draw inside an iframe with their own hard-coded text
    // colours, which are unreadable on the dark page. The iframe is
    // same-origin, so copy our theme colours into it and keep them in step
    // when the theme changes. See assets/js/theme_toggle.js.
    const root = document.documentElement;
    const STYLE_ID = 'site-theme';

    // Our tokens, from _sass/_tokens.scss, under the names the CSS below uses.
    const TOKENS = {
        '--text': '--color-text',
        '--link': '--color-link',
        '--input-bg': '--color-input-bg',
        '--input-border': '--color-input-border',
        '--error': '--color-error',
    };

    const CSS = `
        body, label, legend, p, li, span,
        .hs-richtext, .legal-consent-container { color: var(--text) !important; }
        a { color: var(--link) !important; }
        .hs-input {
            color: var(--text) !important;
            background-color: var(--input-bg) !important;
            border-color: var(--input-border) !important;
        }
        .hs-error-msg, .hs-error-msgs label { color: var(--error) !important; }
    `;

    function themeFrame(frame) {
        const doc = frame.contentDocument;
        if (!doc || !doc.head) return;
        let style = doc.getElementById(STYLE_ID);
        if (!style) {
            style = doc.createElement('style');
            style.id = STYLE_ID;
            doc.head.appendChild(style);
        }
        const page = getComputedStyle(root);
        const vars = Object.entries(TOKENS)
            .map(([name, token]) => `${name}: ${page.getPropertyValue(token).trim()};`)
            .join(' ');
        style.textContent = `:root { ${vars} } ${CSS}`;
    }

    function themeAll() {
        document.querySelectorAll('iframe.hs-form-iframe').forEach(themeFrame);
    }

    // The form arrives after page load, and HubSpot may rewrite its iframe.
    new MutationObserver(themeAll).observe(document.body, { childList: true, subtree: true });
    document.addEventListener('load', (event) => {
        if (event.target.matches && event.target.matches('iframe.hs-form-iframe')) themeFrame(event.target);
    }, true);

    // Follow the theme switch and the OS preference.
    new MutationObserver(themeAll).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', themeAll);

    themeAll();
});
