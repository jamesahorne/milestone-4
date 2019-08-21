// Functions typing() and typing2() were used from https://www.w3schools.com/howto/howto_js_typewriter.asp

$(document).ready(function() {
    setTimeout(typing, 500);
    setTimeout(typing2, 4000);
    setTimeout(cursor, 2000);
    setTimeout(cursor2, 1900);
    setTimeout(cursor3, 12000);
});

var i = 0;
var j = 0;
var typingText = "Hi.";
var typingText2 = "Welcome to Subify's Issue Tracker site.";

function typing() {
    if (i < typingText.length) {
        document.getElementById("typing").innerHTML += typingText.charAt(i);
        i++;
        setTimeout(typing, 110);
    }
}

function typing2() {
    if (j < typingText2.length) {
        document.getElementById("typing2").innerHTML += typingText2.charAt(j);
        j++;
        setTimeout(typing2, 90);
    }
}

function cursor() {
    $('#cursor').hide();
}

function cursor2() {
    $('#cursor2').css('display', 'inline');
}

function cursor3() {
    $('#cursor2').hide();
}
