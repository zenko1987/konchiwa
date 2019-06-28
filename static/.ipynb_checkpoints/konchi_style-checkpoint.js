$("#tabMenu li a").on("click", function() {
  $("#tabBoxes div").hide();
  $($(this).attr("href")).fadeToggle();
  return false;
});