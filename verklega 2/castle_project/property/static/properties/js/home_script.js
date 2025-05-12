function toggleSlider() {
    const slider = document.getElementById("price-slider");
    slider.style.display = slider.style.display === "block" ? "none" : "block";
}

document.addEventListener("DOMContentLoaded", function () {
    // Price slider functionality
    const minInput = document.getElementById("min-price");
    const maxInput = document.getElementById("max-price");
    const minVal = document.getElementById("min-value");
    const maxVal = document.getElementById("max-value");

    if (minInput && minVal && maxInput && maxVal) {
        // Format initial values
        minVal.textContent = parseInt(minInput.value).toLocaleString() + " ISK";
        maxVal.textContent = parseInt(maxInput.value).toLocaleString() + " ISK";

        // Update displayed values when sliders change
        minInput.addEventListener("input", () => {
            minVal.textContent = parseInt(minInput.value).toLocaleString() + " ISK";
        });

        maxInput.addEventListener("input", () => {
            maxVal.textContent = parseInt(maxInput.value).toLocaleString() + " ISK";
        });
    }

    // Optional: Submit form when slider values change for instant filtering
    const form = document.querySelector(".search-form");
    if (form) {
        minInput?.addEventListener("change", () => form.submit());
        maxInput?.addEventListener("change", () => form.submit());
    }
});