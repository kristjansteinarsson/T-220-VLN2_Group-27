function toggleSlider() {
    const slider = document.getElementById("price-slider");
    slider.style.display = slider.style.display === "block" ? "none" : "block";
    }

    document.addEventListener("DOMContentLoaded", function () {
    const minInput = document.getElementById("min-price");
    const maxInput = document.getElementById("max-price");
    const minVal = document.getElementById("min-value");
    const maxVal = document.getElementById("max-value");

    if (minInput && minVal && maxInput && maxVal) {
        minVal.textContent = parseInt(minInput.value).toLocaleString();
        maxVal.textContent = parseInt(maxInput.value).toLocaleString();

        minInput.addEventListener("input", () => {
        minVal.textContent = parseInt(minInput.value).toLocaleString();
        });

        maxInput.addEventListener("input", () => {
        maxVal.textContent = parseInt(maxInput.value).toLocaleString();
        });
    }
    });
