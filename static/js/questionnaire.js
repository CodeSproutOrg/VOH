let start_button_id = 'start-button'
let page_title_id = 'user-form-description'
let questionnaire_id = 'user-form-questionnaire'

let start_button = document.getElementById(start_button_id);
start_button = start_button.addEventListener('click', start_questionnaire);

function start_questionnaire() {
    let page_title = document.getElementById(page_title_id);
    let questionnaire = document.getElementById(questionnaire_id);

    if (questionnaire.style.display == '') {
        questionnaire.style.display = 'flex';
        page_title.style.display = 'none';
    }
}