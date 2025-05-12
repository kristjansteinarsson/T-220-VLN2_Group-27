document.addEventListener("DOMContentLoaded", () => {
    const personalBtn = document.getElementById("personal");
    const agencyBtn = document.getElementById("agency");

    if (personalBtn && agencyBtn) {
        personalBtn.addEventListener("click", () => {
            selectType('personal');
        });

        agencyBtn.addEventListener("click", () => {
            selectType('agency');
        });
    }
});

function selectType(type) {
    const personalBtn = document.getElementById("personal");
    const agencyBtn = document.getElementById("agency");
    const accountType = document.getElementById("account_type");
    
    personalBtn.classList.remove("selected");
    agencyBtn.classList.remove("selected");
    document.getElementById(type).classList.add("selected");
    accountType.value = type;
}