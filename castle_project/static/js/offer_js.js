document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll('.method-btn');
    const forms = document.querySelectorAll('.payment-method');

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            buttons.forEach(b => b.classList.remove('active'));
            forms.forEach(f => f.classList.remove('active'));

            btn.classList.add('active');
            const selectedForm = document.getElementById(btn.dataset.method);
            if (selectedForm) selectedForm.classList.add('active');
        });
    });
});

// Handle form submission
function submitOffer(event) {
    event.preventDefault();
    alert("Purchase offer made for the property at: {{ property.address }}");
    window.location.href = "/";
}
