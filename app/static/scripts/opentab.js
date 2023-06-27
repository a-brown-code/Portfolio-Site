function openTab(memberType, memberId) {
    // Hide all tab content
    var tabContents = document.getElementsByClassName('timeline');
    for (var i = 0; i < tabContents.length; i++) {
        tabContents[i].classList.remove('active');
    }
  
    // Show the selected tab content
    var selectedTabContent = document.getElementById('content-' + memberType + '-' + memberId);
    selectedTabContent.classList.add('active');

    // Sets the active tab button
    var tabButtons = document.getElementsByClassName('tab-button');
    for (var i = 0; i < tabButtons.length; i++) {
        tabButtons[i].classList.remove('active');
    }
    var selectedTabButton = document.getElementById('tab-' + memberType + '-' + memberId);
    selectedTabButton.classList.add('active');
}