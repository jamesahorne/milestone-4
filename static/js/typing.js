$(document).ready(function() {
    setTimeout(typing, 500);
    setTimeout(typing2, 1500);
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
        setTimeout(typing2, 55);
    }
}
