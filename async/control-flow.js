var async = require('async');


/*
async.parallel([
    function(callback){
        setTimeout(function(){
            callback(null, 'one');
        }, 200);
    },
    function(callback){
        setTimeout(function(){
            callback(null, 'two');
        }, 100);
    },
    function(callback){
        setTimeout(function(){
            var err = new Error('I am the error');
            callback(err);
        }, 400);
    },
    function(callback){
        setTimeout(function(){
            callback(null, 'three');
        }, 600);
    },
],
// optional callback
function(err, results){
    if(err){
        console.log('Error', err);
    } else {

    }
    console.log(results);
    //results is now equal to [ 'one', 'two', undefined ]
    // the second function had a shorter timeout.
});
*/

/*
async.series([
   function(callback){
        setTimeout(function(){
            callback(null, 'one');
        }, 200);
    },
    function(callback){
        setTimeout(function(){
            callback(null, 'two');
        }, 100);
    },
    function(callback){
        setTimeout(function(){
            var err = new Error('I am the error');
            callback(err);
        }, 400);
    },
    function(callback){
        setTimeout(function(){
            callback(null, 'three');
        }, 600);
    }
],
// optional callback
function(err, results){
    //results is now equal to [ 'one', 'two', undefined ]
    if(err){
        console.log('Error');
    } else {

    }
    console.log(results);
});

*/


var count = 0;

async.whilst(
    function () {
      console.log(count);
      return count < 5; },
    function (callback) {
        count++;
        setTimeout(callback, 1000);
    },
    function (err) {
        // 5 seconds have passed
    }
);
