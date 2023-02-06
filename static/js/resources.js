let link_button = document.getElementById('link-btn');
let video_btn = document.getElementById('video-btn');
let document_btn = document.getElementById('document-btn');
let app_btn = document.getElementById('app-btn');

console.log(app_btn)

link_button = link_button.addEventListener('click', open_link.bind(null,1));
video_btn = video_btn.addEventListener('click', open_link.bind(null,2));
document_btn = document_btn.addEventListener('click', open_link.bind(null,3));
app_btn = app_btn.addEventListener('click', open_link.bind(null,4));

function open_link(number) {
    let links = document.getElementById('links');
    let videos = document.getElementById('videos');
    let documents = document.getElementById('documents');
    let apps = document.getElementById('apps');

    switch (number) {
        case 1:
            videos.classList.remove('active');
            videos.style.padding = '0';
            documents.classList.remove('active');
            apps.classList.remove('active');

            links.classList.add('active');
            break
        case 2:
            videos.classList.add('active');
            videos.style.padding = '5%';

            links.classList.remove('active');
            documents.classList.remove('active');
            apps.classList.remove('active');
            break
        case 3:
            documents.classList.add('active');

            links.classList.remove('active');
            videos.classList.remove('active');
            videos.style.padding = '0';
            apps.classList.remove('active');
            break

        case 4:
            apps.classList.add('active');

            links.classList.remove('active');
            documents.classList.remove('active');
            videos.classList.remove('active');
            videos.style.padding = '0';

            break
    }
}





//let scroll_buttons = document.getElementsByClassName('resources-navigation-btn');


//for (let button_number = 0; button_number < scroll_buttons.length; button_number++) {
//    scroll_button = scroll_buttons[button_number];
//    scroll_button.addEventListener('click', function scroll() {
//        scroll_to[button_number].scrollIntoView({
//            behavior: "smooth",
//            block: "start"
//        });
//    });
//}
