var async = require('async');
var fs = require('fs');

/*
function printf(item) {
  console.log(item);
  return item
}

function printf2(item) {
  return item
}

async.map(['1.txt', '2.txt', '3.txt'], printf, function (err, results) {
  console.log(results);
});

async.each(['11.txt', '22.txt', '33.txt'], printf, function (err, results) {
  console.log(results);
});

async.each(['111.txt', '222.txt', '333.txt'], function (item, callback) {
  console.log('>', item);
  // callback();
});
*/

/*
async.each([0,1,2,3,4,5,6,7,8,9], function(item, callback) {
  setTimeout(function() {
    console.log('>', item);
    callback();
  }, 2 * Math.random() * 1000);
}, function(err) {
  console.log('> done');
});

console.log(':)');
*/

/*
async.each([0,1,2,3,4,5,6,7,8,9], function(item, callback) {
  setTimeout(function() {
    console.log('>', item);
    if (item === 3) {
      callback("error: This item eque 3");
    }
    else {
      callback();
    }
  }, 2 * Math.random() * 1000);
}, function(err) {
  if (err) {
    console.log('some error');
    console.log(err);
  }
  else {
    console.log('success');
  }
  console.log('> done');
});

console.log(':)');
*/


/*
async.each([0,1,2,3,4,5,6,7,8,9], function(item, callback) {
  if (item === 3) {
    setTimeout(function () {
      console.log('>', item);
      callback('123;qqq');
    }, 1000);
  }
  else {
    console.log('>', item);
    callback();
  }
}, function(err) {
  console.log('> done');
});

console.log(':)');
*/


/*
async.eachSeries([0,1,2,3,4,5,6,7,8,9], function(item, callback) {
  if (item === 3) {
    setTimeout(function () {
      console.log('>', item);
      callback('123123');
    }, 1000);
  }
  else {
    console.log('>', item);
    callback();
  }
}, function(err) {
  if (err) console.log(err);
  console.log('> done');
});

console.log(':)');
*/


/*
async.eachLimit([0,1,2,3,4,5,6,7,8,9], 1, function(item, callback) {
  if (item === 3) {
    setTimeout(function () {
      console.log('>', item);
      callback('123');
    }, 1000);
  }
  else {
    console.log('>', item);
    callback();
  }
}, function(err) {
  if (err) console.log(err);
  console.log('> done');
});

console.log(':)');

*/



/*
var obj = {one: '1', two: '2', three: '3'};

async.forEachOf(obj, function (value, key, callback) {
  console.log(key, value);
  callback();
}, function (err) {
  if (err) console.log(err);
  console.log("> done");
})
*/


/*
async.map([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], function (item, callback) {
  if (item === 3) {
    setTimeout(function () {
      callback(null, item + 10)
    }, 1000);
  }
  else {
    callback(null, item + 10)
  }
}, function (err, result) {
  console.log(result);
});
*/

/*
async.filter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], function (item, callback) {
  if (item % 2 === 0) {
    callback(true);
  }
  else {
    callback(false);
  }
}, function (results) {
  console.log(results);
})
*/


/*
async.reduce([1,2,3], 0, function(memo, item, callback){
    // pointless async:
    process.nextTick(function(){
        callback(null, memo + item)
    });
}, function(err, result){
    console.log(result);
    // result is now equal to the last value of memo, which is 6
});
*/


// 正序排序
async.sortBy([1,9,3,5], function(x, callback){
  callback(null, x);
}, function(err,result){
  console.log(result);
});

// 逆序排序
async.sortBy([1,9,3,5], function(x, callback){
    callback(null, x*-1);    //<- x*-1 instead of x, turns the order around
}, function(err,result){
  console.log(result);
});




































