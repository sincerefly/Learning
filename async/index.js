var async = require('async');
var fs = require('fs');

function printf(item) {
  console.log(item);
}

/* 文件状态 */
async.map(['1.txt', '2.txt', '3.txt'], fs.stat, function (err, results) {
  console.log(results);
});

/* 存在的文件 */
/*
async.filter(['1.txt', '2.txt', '3.txt'], fs.exists, function (results) {
  for (var i in results) {
    console.log(results[i]);
  }
});
*/
