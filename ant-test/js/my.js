/* 侧边栏响应 */

// 新建文章
$(function() {
  $(document).on('click', '#new', function() {
    $('.main-container').load("tiles/new.html");
  });
});

// 文章列表
$(function() {
  $(document).on('click', '#list', function() {
    $('.main-container').load("tiles/list.html");
    // 载入列表数据
    $.getJSON("http://127.0.0.1:3000/list", function (json, status) {
      $("#getlist").html("");
      $.each(json['data'], function (i, item) {
        $("#artlist").append(
          "<li>" + item.title + "</li>"
        );
      });
    });
  });
});

// Hexo设置
$(function () {
  $(document).on('click', '#hexo_settings', function() {
    $('.main-container').load("tiles/hexo_settings.html");
    // 载入Hexo配置文件数据
    $.getJSON("http://127.0.0.1:3000/hexo_settings", function (json, status) {
      $("#settings").append(
        json['data']
      );
    });
  });
});

/* 新建文章 */
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

/*
$(function () {
  $(document).on("onload", "#getlist", function () {
    $.getJSON("http://127.0.0.1:3000/list", function (json, status) {
      $("#getlist").html("");
      $.each(json['data'], function (i, item) {
        $("#artlist").append(
          "<li>" + item.title + "</li>"
        );
      });
    });
  });
})
*/
