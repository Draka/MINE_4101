var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render('example', { title: 'MINE 4101 - Ejemplo' });
});

module.exports = router;
