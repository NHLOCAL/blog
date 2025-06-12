document.addEventListener('DOMContentLoaded', function () {
    // 1. Reading Progress Bar
    const progressBar = document.getElementById('reading-progress-bar');
    if (progressBar) {
        window.addEventListener('scroll', () => {
            const totalHeight = document.body.scrollHeight - window.innerHeight;
            const progress = (window.pageYOffset / totalHeight) * 100;
            progressBar.style.width = `${progress}%`;
        });
    }

    // 2. Code Block "Copy" Button
    const codeBlocks = document.querySelectorAll('div.highlight');
    codeBlocks.forEach(block => {
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-code-button';
        copyButton.innerHTML = '<i class="bi bi-clipboard"></i> <span>העתק</span>';
        block.appendChild(copyButton);

        copyButton.addEventListener('click', () => {
            const code = block.querySelector('pre code').innerText;
            navigator.clipboard.writeText(code).then(() => {
                const buttonText = copyButton.querySelector('span');
                buttonText.innerText = 'הועתק!';
                copyButton.classList.add('copied');
                setTimeout(() => {
                    buttonText.innerText = 'העתק';
                    copyButton.classList.remove('copied');
                }, 2000);
            });
        });
    });
});