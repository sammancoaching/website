document.addEventListener('DOMContentLoaded', () => {
    const ICONS = {
        copy: `<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>`,
        success: `<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#155724" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`,
        error: `<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#721c24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg>`
    };

    const codeBlocks = document.querySelectorAll('div.highlighter-rouge, figure.highlight, pre, blockquote');

    codeBlocks.forEach((block) => {
        const container = block.closest('div.highlighter-rouge, figure.highlight') || block;
        if (container.querySelector('.copy-code-button')) return;

        if (getComputedStyle(container).position === 'static') {
            container.style.position = 'relative';
        }

        const button = document.createElement('button');
        button.className = 'copy-code-button';
        button.type = 'button';
        button.innerHTML = ICONS.copy;
        button.ariaLabel = 'Copy to clipboard';

        const codeElement = block.querySelector('code') || block;

        button.addEventListener('click', () => {
            const code = codeElement.innerText;
            navigator.clipboard.writeText(code)
                .then(() => updateButtonState(button, 'success'))
                .catch(() => updateButtonState(button, 'error'));
        });

        container.appendChild(button);
    });

    /**
     * Updates the copy button state briefly to show success or error feedback.
     * @param {HTMLButtonElement} button
     * @param {'success'|'error'} state
     */
    function updateButtonState(button, state) {
        if (button.dataset.timeout) {
            clearTimeout(parseInt(button.dataset.timeout, 10));
        }

        button.innerHTML = ICONS[state];
        button.classList.toggle('copied', state === 'success');
        button.classList.toggle('error', state === 'error');

        const timeoutId = setTimeout(() => {
            button.innerHTML = ICONS.copy;
            button.classList.remove('copied', 'error');
            delete button.dataset.timeout;
        }, 2000);

        button.dataset.timeout = timeoutId.toString();
    }
});
