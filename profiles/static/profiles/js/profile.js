let defaultCountySelectEl = document.getElementById("id_default_county");

for (let option of defaultCountySelectEl) {
    if (option.text === "County *") {
        option.setAttribute("disabled", "");
        option.setAttribute("selected", "");
        option.classList.add("text-muted");
    }
}