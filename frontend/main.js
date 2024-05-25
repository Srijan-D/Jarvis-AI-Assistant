$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        }

    });

    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "2",
        speed: "0.10",
        autostart: true

    });
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    // mic on click
    $("#mic-btn").click(function () {
        eel.playAssistantSound()
        $("#oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()
    })

    function keyUp(e) {

        if (e.key == 'j' && e.metaKey) { //metaKey is for command key in mac and windows key in windows
            eel.playAssistantSound()
            $("#oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()
        }
    }
    document.addEventListener('keyup', keyUp, false); //false is for bubbling means it will not go to parent element

    function PlayAssistant(message) {

        if (message != "") {
            $("#oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#mic-btn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);

        }
    }

    // toggle between mic and send button
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#mic-btn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#mic-btn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }

    // Keyup event handler for text box
    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)

    });

    // Event handler on send button
    $("#SendBtn").click(function () {
        let message = $("#chatbox").val()
        PlayAssistant(message)
    });

    // Press enter button to send message
    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) { //13 is the enter key
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });
});

