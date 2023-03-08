var axios = require('axios');
var qs = require('qs');
var data = qs.stringify({
  'code': 'effsfsefes' 
});
var config = {
  method: 'post',
maxBodyLength: Infinity,
  url: 'http://boburbem.beget.tech/',
  headers: { 
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
