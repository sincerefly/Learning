$(function() {
  $(document).on('click', '#new', function() {
    $('.main-container').load("tiles/new.html");
  });
});


$(function() {
  $(document).on('click', '#list', function() {
    $('.main-container').load("tiles/list.html");
  });
});

$(function() {
  $(document).on("click", '#create', function() {
    alert("hello world!");
  });
});



