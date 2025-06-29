document.addEventListener("DOMContentLoaded", function () {
    const testimonials = document.querySelector(".testimonials");
    let scrollAmount = 0;

    setInterval(() => {
        scrollAmount += 300;
        if (scrollAmount >= testimonials.scrollWidth - testimonials.clientWidth) {
            scrollAmount = 0;
        }
        testimonials.scrollTo({ left: scrollAmount, behavior: "smooth" });
    }, 3000);
});
