$(function() {
  $("#box").css("color", "red");
});

$(function () {
  alert(document.getElementById('box'));
});

$(function () {
  alert($('#box').get(0));
});
