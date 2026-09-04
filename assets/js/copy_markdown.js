document.addEventListener('DOMContentLoaded', () => {
    // How long the outcome stays visible after the pointer leaves the button.
    const FEEDBACK_LINGER_MS = 2000;
    // Matches the label's collapse transition in _sass/_copy_markdown.scss.
    const LABEL_COLLAPSE_MS = 300;

    document.querySelectorAll('.copy-markdown').forEach((container) => {
        const button = container.querySelector('.copy-markdown-button');
        const label = container.querySelector('.copy-markdown-label');
        const source = container.querySelector('.copy-markdown-source');
        if (!button || !label || !source) return;

        const idleText = label.textContent;
        let revertTimeout = null;

        button.addEventListener('click', () => {
            navigator.clipboard.writeText(source.textContent)
                .then(() => showFeedback('copied', 'Copied ✓'))
                .catch(() => showFeedback('error', 'Copy failed'));
        });

        // The outcome stays while the button is hovered or focused, so the
        // reader has time to see it; leaving it starts the countdown.
        button.addEventListener('mouseleave', scheduleRevert);
        button.addEventListener('blur', scheduleRevert);

        /**
         * Shows the outcome in the button's label until the reader moves on.
         * @param {'copied'|'error'} state
         * @param {string} text
         */
        function showFeedback(state, text) {
            clearTimeout(revertTimeout);
            label.textContent = text;
            button.classList.toggle('copied', state === 'copied');
            button.classList.toggle('error', state === 'error');
            scheduleRevert();
        }

        function scheduleRevert() {
            if (!button.classList.contains('copied') && !button.classList.contains('error')) return;
            clearTimeout(revertTimeout);
            revertTimeout = setTimeout(revert, FEEDBACK_LINGER_MS);
        }

        /**
         * Collapses the label straight back to the icon, keeping the outcome
         * text during the collapse so it never flashes the idle text.
         */
        function revert() {
            if (button.matches(':hover') || button.matches(':focus-visible')) return;
            button.classList.remove('copied', 'error');
            revertTimeout = setTimeout(() => {
                label.textContent = idleText;
            }, LABEL_COLLAPSE_MS);
        }
    });
});
