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


    eel.expose(senderText)
    function senderText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            // Append the message to the chat box towards the right
            chatBox.innerHTML += `<div class="row justify-content-end mb-4">
            <div class = "width-size">
            <div class="sender_message">${message}</div>
        </div>`;
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    eel.expose(receiverText)
    function receiverText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            // Append the message to the chat box towards the left
            chatBox.innerHTML += `<div class="row justify-content-start mb-4">
            <div class = "width-size">
            <div class="receiver_message">${message}</div>
            </div>
        </div>`;

            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }

    }


})

