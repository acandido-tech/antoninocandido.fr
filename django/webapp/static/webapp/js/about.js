$("div .logo-couleurs").css("opacity", 0);
$(".logo-couleurs").hover(function () {
    $(this).fadeTo("fast", 1.0); // This should set the opacity to 100% on hover
}, function () {
    $(this).fadeTo("fast", 0); // This should set the opacity back to 0% on mouseout
});