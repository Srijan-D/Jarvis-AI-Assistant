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
        eel.takecommand()
    })

});

