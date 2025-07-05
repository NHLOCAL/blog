document.addEventListener('DOMContentLoaded', function () {

    const progressBar = document.getElementById('reading-progress-bar');
    if (progressBar) {
        window.addEventListener('scroll', () => {
            const totalHeight = document.body.scrollHeight - window.innerHeight;
            const progress = (window.pageYOffset / totalHeight) * 100;
            progressBar.style.width = `${progress}%`;
        });
    }


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

    // --- Dynamic Feedback Link ---
    (function setDynamicFeedbackLink() {
        const email = 'nh.local11@gmail.com';
        const subject = encodeURIComponent('משוב על הבלוג');
        const body = encodeURIComponent('שלום,');
        
        const isWindows = navigator.platform.toLowerCase().indexOf('win') > -1;
        
        let feedbackUrl;
        if (isWindows) {
            // Use Gmail link for Windows users
            feedbackUrl = `https://mail.google.com/mail/?view=cm&fs=1&to=${email}&su=${subject}&body=${body}`;
        } else {
            // Use standard mailto for other OS (Mac, Linux, iOS, Android)
            feedbackUrl = `mailto:${email}?subject=${subject}&body=${body}`;
        }

        const headerLink = document.getElementById('feedback-link-header');
        if (headerLink) {
            headerLink.href = feedbackUrl;
            // Open in new tab for external Gmail link
            if(isWindows) headerLink.target = '_blank';
        }

        const sidebarLink = document.getElementById('feedback-link-sidebar');
        if (sidebarLink) {
            sidebarLink.href = feedbackUrl;
             // Open in new tab for external Gmail link
            if(isWindows) sidebarLink.target = '_blank';
        }
    })();
});