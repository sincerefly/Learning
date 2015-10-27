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

/*
$(function() {
  $(document).on("click", '#create', function() {
    alert("hello world!");
  });
});
*/

$(function () {
  $(document).on("click", '#create', function () {
    alert($('input[name=title]').val());
    $.ajax({
      type: 'POST',
      url: 'http://127.0.0.1:3000/new',
      data: {
        title: $('input[name=title]').val(),
        date: $('input[name=date]').val(),
        filename: $('input[name=filename]').val(),
        tags: $('input[name=tags]').val(),
        content: $('textarea[name=content]').val()
      },
      success: function (res, status, xhr) {
        alert('success!: ' + res.title);
      }
    })
  })
})

