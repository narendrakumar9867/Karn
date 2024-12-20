$(document).ready(function () {
    
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },
    });

    // Siri Configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 600,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
      });

    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            effect: true
        },
        out: {
            effect: "fadeOutUp",
            effect: true
        },
    });

    // mic button click event

    $("#MicBtn").click(function () { 
        eel.playAssistantsound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);

    });

});