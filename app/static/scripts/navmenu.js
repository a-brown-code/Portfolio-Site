function toggleNav() {
    var nav = document.getElementById("toggle-menu");
    var icon = document.getElementById("icon");
    if (nav.style.right === "0px") {
        nav.style.right = "-50%";
        icon.classList.remove("fa-times");
        icon.classList.add("fa-bars");
    }
    else {
        nav.style.right = "0px";
        icon.classList.remove("fa-bars");
        icon.classList.add("fa-times");
    }
}