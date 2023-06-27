function openWorkTab(activePerson) {

    // Switch active work experiences

    var allWork = document.getElementsByClassName("work-experience");
    for (var i = 0; i < allWork.length; i++) {
        if (allWork[i].classList.contains('active') && !allWork[i].classList.contains(activePerson)) {
            allWork[i].classList.replace('active', 'inactive');
        }
        else if (allWork[i].classList.contains('inactive') && allWork[i].classList.contains(activePerson)) {
            allWork[i].classList.replace('inactive', 'active');
        }
    }

    // Switch active buttons

    var allButtons = document.getElementsByClassName("work-selector-button");
    for (var i = 0; i < allButtons.length; i++) {
        if (allButtons[i].classList.contains('active') && !allButtons[i].classList.contains(activePerson)) {
            allButtons[i].classList.replace('active', 'inactive');
        }

        else if (allButtons[i].classList.contains('inactive') && allButtons[i].classList.contains(activePerson)) {
            allButtons[i].classList.replace('inactive', 'active');
        }
    }

}