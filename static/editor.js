document.addEventListener('DOMContentLoaded', () => {

    // Function: Connects input to preview, and hides the section if empty
    function bindField(inputId, previewId, wrapperId, isInline = false) {
        const inputElement = document.getElementById(inputId);
        const previewElement = document.getElementById(previewId);
        const wrapperElement = document.getElementById(wrapperId);

        if (!inputElement || !previewElement) return;

        function updateView() {
            const val = inputElement.value.trim();
            previewElement.innerText = val;

            // Hiding Logic
            if (val === "") {
                if (wrapperElement) wrapperElement.style.display = "none";
            } else {
                if (wrapperElement) {
                    wrapperElement.style.display = isInline ? "inline-flex" : "block";
                }
            }
        }

        // Run instantly when typing
        inputElement.addEventListener('input', updateView);
        // Run once on page load
        updateView();
    }

    // 1. HEADER DETAILS (Inline hiding)
    bindField('nameInput', 'previewName', null); // Name never hides
    bindField('roleInput', 'previewRole', null); // Role never hides
    bindField('phoneInput', 'previewPhone', 'wrapPhone', true);
    bindField('emailInput', 'previewEmail', 'wrapEmail', true);
    bindField('locationInput', 'previewLocation', 'wrapLocation', true);
    bindField('githubInput', 'previewGithub', 'wrapGithub', true);
    bindField('linkedinInput', 'previewLinkedin', 'wrapLinkedin', true);
    bindField('portfolioInput', 'previewPortfolio', 'wrapPortfolio', true);

    // 2. MAIN SECTIONS (Block hiding - hides the whole heading if empty)
    bindField('summaryInput', 'previewSummary', 'secSummary');
    bindField('eduInput', 'previewEdu', 'secEdu');
    bindField('techInput', 'previewTech', 'secTech');
    bindField('softInput', 'previewSoft', 'secSoft');
    bindField('langInput', 'previewLang', 'secLang');
    bindField('certInput', 'previewCert', 'secCert');
    bindField('expInput', 'previewExp', 'secExp');
    bindField('projInput', 'previewProj', 'secProj');

    // PDF Download Setup
    const downloadBtn = document.getElementById('download-pdf');
    if (downloadBtn) {
        downloadBtn.addEventListener('click', () => {
            const element = document.getElementById('resumePreview');
            const opt = {
                margin:       0,
                filename:     'my-resume.pdf',
                image:        { type: 'jpeg', quality: 0.98 },
                html2canvas:  { scale: 2 },
                jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
            };
            html2pdf().set(opt).from(element).save();
        });
    }
});