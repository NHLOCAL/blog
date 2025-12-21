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


    (function setDynamicFeedbackLink() {
        const email = 'nh.local11@gmail.com';
        const subject = encodeURIComponent('משוב על הבלוג');
        const body = encodeURIComponent('שלום,');

        const isWindows = navigator.platform.toLowerCase().indexOf('win') > -1;

        let feedbackUrl;
        if (isWindows) {

            feedbackUrl = `https://mail.google.com/mail/?view=cm&fs=1&to=${email}&su=${subject}&body=${body}`;
        } else {

            feedbackUrl = `mailto:${email}?subject=${subject}&body=${body}`;
        }

        const headerLink = document.getElementById('feedback-link-header');
        if (headerLink) {
            headerLink.href = feedbackUrl;

            if(isWindows) headerLink.target = '_blank';
        }

        const sidebarLink = document.getElementById('feedback-link-sidebar');
        if (sidebarLink) {
            sidebarLink.href = feedbackUrl;

            if(isWindows) sidebarLink.target = '_blank';
        }
    })();

    // --- Share Button Logic (New) ---
    const copyLinkBtn = document.getElementById('copy-link-btn');
    if (copyLinkBtn) {
        copyLinkBtn.addEventListener('click', async () => {
            try {
                await navigator.clipboard.writeText(window.location.href);
                
                // Show feedback
                const feedbackMsg = document.getElementById('copy-feedback');
                const icon = copyLinkBtn.querySelector('i');
                
                // Change icon temporarily
                icon.classList.remove('bi-link-45deg');
                icon.classList.add('bi-check-lg');
                
                if (feedbackMsg) feedbackMsg.classList.add('show');
                
                setTimeout(() => {
                    icon.classList.remove('bi-check-lg');
                    icon.classList.add('bi-link-45deg');
                    if (feedbackMsg) feedbackMsg.classList.remove('show');
                }, 2000);
                
            } catch (err) {
                console.error('Failed to copy: ', err);
            }
        });
    }
});