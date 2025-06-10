document.addEventListener("DOMContentLoaded", function () {
    const items = document.querySelectorAll(".carousel-item");
    let index = 0;

    setInterval(() => {
        items.forEach(item => item.classList.remove("active"));
        items[index].classList.add("active");
        index = (index + 1) % items.length;
    }, 3000);
});
