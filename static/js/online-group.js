let sign_up_btn = document.getElementById('sign-up-btn');
sign_up_btn = sign_up_btn.addEventListener('click', open_window);

function open_window() {
    let window = document.getElementById('modal');
    window.style.display = 'flex';

    window.scrollIntoView({
            behavior: "smooth",
            block: "center"
    });
}


let close_btn = document.getElementById('close-modal');
close_btn = close_btn.addEventListener('click', close_window)

function close_window() {
    let window = document.getElementById('modal');
    window.style.display = 'none';

    let online_group = document.getElementById('online-group');
    online_group.scrollIntoView({
            behavior: "smooth",
            block: "center"
    });
}