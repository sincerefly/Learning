var dbpath='mongodb://localhost:27017/speak';
var MongoClient = require('mongodb').MongoClient;
var sd = require('silly-datetime');

exports.getData = function (req, res) {

  var finder = {};
  if (req.query.flag === "0") {
    finder = {"flag": 0};
  } else if (req.query.flag === "-1") {
    finder = {"flag": -1};
  } else {
    finder = {"flag": 0};
  }

  MongoClient.connect(dbpath, function(err, db) {
    if (err) {throw err;}

    var collection = db.collection('xmspeak');
    collection.find(finder).toArray(function (err, docs) {
      if (err) {throw err;}

      var i = 0;
      var item = {};
      var data = [];
      for (i=0; i<docs.length; i++) {

        item = {
          "key": i+1,
          "content": docs[i].content,
          "ymd": docs[i].ymd,
          "hms": docs[i].hms,
          "timestamp": docs[i].timestamp,
          "author": docs[i].author,
          "flag": docs[i].flag
        };

        data.push(item);
      }
      console.log('Get data success');
      return res.jsonp({status: 0, result: data, message: "get data success"});
    });
  });
};


exports.speak = function (req, res) {
  console.log(req.body.content);

  var content = req.body.content;

  // get datetime
  var now = new Date();
  var ymd = sd.format(now, 'YYYY-MM-DD');
  var hms = sd.format(now, 'HH:mm:ss');
  var timestamp = now.getTime();

  console.log(ymd);
  console.log(hms);
  console.log(timestamp);

  var json = {
    author: 'xiaoming',
    content: content,
    ymd: ymd,
    hms: hms,
    timestamp: timestamp,
    flag: 0
  };

  MongoClient.connect(dbpath, function (err, db) {
    if (err) { throw err; }
    var collection = db.collection('xmspeak');
    collection.insert(json, function (e, docs) {
      if (e) { throw e; }
      if (docs.result.ok === 1) {
        console.log('add speak to database success');
        db.close();
        return res.jsonp({status:0, result:"", message:"add speak success"});
      }
      console.log('add speak to database failed');
      db.close();
      return res.jsonp({status:-1, result:"", message:"add speak to database failed"});
    });
  });
};


exports.update = function (req, res) {

  var timestamp = req.body.timestamp;
  var content = req.body.content;

  if (!timestamp) {
    return res.jsonp({status:-1, result:"rm speak fail", message:"no timestamp"});
  }

  var json = {
    timestamp: parseFloat(timestamp)
  };

  MongoClient.connect(dbpath, function (err, db) {
    if (err) { throw err; }

    var collection = db.collection('xmspeak');
    collection.update(json, {$set: {"content": content}}, function (e, docs) {
      if (e) { throw e; }
      if (docs.result.ok === 1) {
        console.log('update ok');
        return res.jsonp({status:0, result:"", message:"update speak success"});
      } else {
        console.log('update fail');
        return res.jsonp({status:-1, result:"", message:"update speak fail"});
      }
    });
  });
};


exports.rm = function (req, res) {

  var timestamp = req.query.timestamp;

  console.log(timestamp);

  if (!timestamp) {
    return res.jsonp({status:-1, result:"rm speak fail", message:"no timestamp"});
  }

  var json = {
    timestamp: parseFloat(timestamp)
  };

  MongoClient.connect(dbpath, function (err, db) {
    if (err) { throw err; }

    var collection = db.collection('xmspeak');
    collection.update(json, {$set: {"flag": -1}}, function (e, docs) {
      if (e) { throw e; }
      if (docs.result.ok === 1) {
        console.log('rm ok');
        return res.jsonp({status:0, result:"", message:"rm speak success"});
      } else {
        console.log('rm fail');
        return res.jsonp({status:-1, result:"", message:"rm speak fail"});
      }
    });
  });
};


exports.active = function (req, res) {

  var timestamp = req.query.timestamp;

  if (!timestamp) {
    return res.jsonp({status:-1, result:"active speak fail", message:"no timestamp"});
  }

  var json = {
    timestamp: parseFloat(timestamp)
  };

  MongoClient.connect(dbpath, function (err, db) {
    if (err) { throw err; }

    var collection = db.collection('xmspeak');
    collection.update(json, {$set: {"flag": 0}}, function (e, docs) {
      if (e) { throw e; }
      if (docs.result.ok === 1) {
        console.log('active ok');
        return res.jsonp({status:0, result:"", message:"active speak success"});
      } else {
        console.log('active fail');
        return res.jsonp({status:-1, result:"", message:"active speak fail"});
      }
    });
  });
};






