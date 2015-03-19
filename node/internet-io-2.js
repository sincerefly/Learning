var http = require('http');

http.get({host: 'www.baidu.com'}, function(res) {
  console.log('Get response: ' + res.statusCode);
}).on('error', function(e) {
  console.log('Got error: ' + e.message);
});
