let scroll_button = document.getElementById('main-page-btn');
let scroll_to = document.getElementById('who-we-are-content');

scroll_button = scroll_button.addEventListener('click', scroll)

function scroll() {
    scroll_to.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });
}