var http = require('follow-redirects').http;
var fs = require('fs');

var qs = require('querystring');

var options = {
  'method': 'POST',
  'hostname': 'boburbem.beget.tech',
  'path': '/',
  'headers': {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  'maxRedirects': 20
};

var req = http.request(options, function (res) {
  var chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function (chunk) {
    var body = Buffer.concat(chunks);
    console.log(body.toString());
  });

  res.on("error", function (error) {
    console.error(error);
  });
});

var postData = qs.stringify({
  'code': 'effsfsefes'
});

req.write(postData);

req.end();



console.log("hello")