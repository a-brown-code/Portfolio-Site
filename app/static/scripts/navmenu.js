function toggleNav() {
    const nav = document.getElementById("toggle-menu");
    const icon = document.getElementById("icon");
    const isOpen = nav.style.right === "0px";
    nav.style.right = isOpen ? "-50%" : "0px";
    icon.classList.toggle("fa-bars", isOpen);
    icon.classList.toggle("fa-times", !isOpen);
}