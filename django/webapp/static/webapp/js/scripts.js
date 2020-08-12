(function ($) {
  "use strict"; // Start of use strict

  // init parallaxSlider
  $('#pxs_container').parallaxSlider();

  $("#hov-1").css("opacity", 0);
  $("#hov-2").css("opacity", 0);
  $('.item li div.info_cache').css("opacity", 0);

  $("#hov-1").hover(function () {
    $(this).stop().fadeTo("slow", 1.0); // This should set the opacity to 100% on hover
  }, function () {
    $(this).stop().fadeTo("slow", 0); // This should set the opacity back to 0% on mouseout
  });

  $("#hov-2").hover(function () {
    $(this).stop().fadeTo("slow", 1.0); // This should set the opacity to 100% on hover
  }, function () {
    $(this).stop().fadeTo("slow", 0); // This should set the opacity back to 0% on mouseout
  });


})(jQuery); // End of use strict
