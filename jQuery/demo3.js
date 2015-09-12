$(function () {
  $('#haha').on('mouseover mouseout', {name: 'lxd', age: '23'}, function (e) {
    alert('hello world' + e.data.name);
  });
});
