let link_button = document.getElementById('link-btn');
let video_btn = document.getElementById('video-btn');
let document_btn = document.getElementById('document-btn');
let app_btn = document.getElementById('app-btn');

link_button = link_button.addEventListener('click', open_link.bind(null,1));
video_btn = video_btn.addEventListener('click', open_link.bind(null,2));
document_btn = document_btn.addEventListener('click', open_link.bind(null,3));
app_btn = app_btn.addEventListener('click', open_link.bind(null,4));

function open_link(number) {
    let links = document.getElementById('links');
    let videos = document.getElementById('videos');
    let documents = document.getElementById('documents-section');
    let apps = document.getElementById('apps');

    switch (number) {
        case 1:
            videos.classList.remove('active');
            documents.classList.remove('active');
            apps.classList.remove('active');

            links.classList.add('active');
            break
        case 2:
            links.classList.remove('active');
            documents.classList.remove('active');
            apps.classList.remove('active');

            videos.classList.add('active');
            break
        case 3:
            links.classList.remove('active');
            videos.classList.remove('active');
            apps.classList.remove('active');

            documents.classList.add('active');
            break

        case 4:
            links.classList.remove('active');
            documents.classList.remove('active');
            videos.classList.remove('active');

            apps.classList.add('active');
            break
    }
}
