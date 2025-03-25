// Form handling
document.addEventListener('DOMContentLoaded', () => {
    // Fraud detection form
    const fraudForm = document.getElementById('fraudForm');
    if(fraudForm) {
        fraudForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(fraudForm);
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });
            if(response.ok) {
                window.location.href = '/result';
            }
        });
    }

    // Transfer form handling
    const transferForm = document.getElementById('transferForm');
    if(transferForm) {
        transferForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            // Add transfer logic
        });
    }
});