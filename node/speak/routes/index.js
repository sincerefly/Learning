var express = require('express');
var router = express.Router();

/* GET home page. */
var index = require('../controllers/index.js');

router.get('/getData', index.getData);
router.get('/rm', index.rm);
router.get('/active', index.active);
router.post('/speak', index.speak);
router.post('/update', index.update);


module.exports = router;
