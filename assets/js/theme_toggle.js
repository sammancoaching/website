document.addEventListener('DOMContentLoaded', () => {
    // The header switch between light and dark. The choice is saved, and
    // _includes/head.html applies it on the next page before it draws.
    // With no saved choice the page uses the site default from _sass/_tokens.scss.
    const root = document.documentElement;
    const button = document.querySelector('.theme-toggle');
    if (!button) return;

    // _tokens.scss sets color-scheme on :root, so this is the theme actually showing.
    const isDark = () => getComputedStyle(root).colorScheme === 'dark';

    function showState() {
        button.setAttribute('aria-pressed', String(isDark()));
    }

    button.addEventListener('click', () => {
        const theme = isDark() ? 'light' : 'dark';
        root.setAttribute('data-theme', theme);
        try {
            localStorage.setItem('theme', theme);
        } catch (e) {
            // Storage can be blocked; the switch still works for this page.
        }
        showState();
    });

    // Keep the button in step if the default follows the OS and that changes.
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', showState);

    showState();
});
