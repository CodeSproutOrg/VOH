let scroll_buttons = document.getElementsByClassName('navigation-btn');
scroll_to = document.getElementsByClassName('link-title');

for (let button_number = 0; button_number < scroll_buttons.length; button_number++) {
    scroll_button = scroll_buttons[button_number];
    scroll_button.addEventListener('click', function scroll() {
        scroll_to[button_number].scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    });
}




