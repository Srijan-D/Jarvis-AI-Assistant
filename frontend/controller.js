$(document).ready(function () {

    //display the messages in the chat window
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $('.siri-message li:first').text(message);
        $('.siri-message').textillate('start');
    }
    // Display home screen
    eel.expose(ShowHome)
    function ShowHome() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }

})

