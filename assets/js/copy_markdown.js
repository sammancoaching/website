document.addEventListener('DOMContentLoaded', () => {
    const FEEDBACK_DURATION_MS = 1500;

    document.querySelectorAll('.copy-markdown').forEach((container) => {
        const button = container.querySelector('.copy-markdown-button');
        const label = container.querySelector('.copy-markdown-label');
        const source = container.querySelector('.copy-markdown-source');
        if (!button || !label || !source) return;

        const idleText = label.textContent;

        button.addEventListener('click', () => {
            navigator.clipboard.writeText(source.textContent)
                .then(() => showFeedback('copied', 'Copied ✓'))
                .catch(() => showFeedback('error', 'Copy failed'));
        });

        /**
         * Shows the outcome in the button's label for a moment, then reverts.
         * @param {'copied'|'error'} state
         * @param {string} text
         */
        function showFeedback(state, text) {
            if (button.dataset.timeout) {
                clearTimeout(parseInt(button.dataset.timeout, 10));
            }

            label.textContent = text;
            button.classList.toggle('copied', state === 'copied');
            button.classList.toggle('error', state === 'error');

            const timeoutId = setTimeout(() => {
                label.textContent = idleText;
                button.classList.remove('copied', 'error');
                delete button.dataset.timeout;
            }, FEEDBACK_DURATION_MS);

            button.dataset.timeout = timeoutId.toString();
        }
    });
});
