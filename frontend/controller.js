$(document).ready(function () {

    //display the messages in the chat window
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $('.siri-message li:first').text(message);
        $('.siri-message').textillate('start');
    }
})

