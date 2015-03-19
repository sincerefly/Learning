var fs = require('fs');

fs.readFile('data.txt', 'utf-8', function (err, data) {
  if (err) throw err;
  console.log('file read: ');
  console.log(data);
});
