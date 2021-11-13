var express = require('express');
const { execSync } = require('child_process');
var router = express.Router();

/* GET users listing. */
router.post('/', function(req, res, next) {
  console.log(req.body);
  let result = execSync(`python3 check.py ${req.body.a1} ${req.body.a2} ${req.body.a3} ${req.body.a4} ${req.body.a5} ${req.body.a6}`);
  res.send({probabilidad: result.toString()});
});

module.exports = router;
