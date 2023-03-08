const http = require("http");

const url = 'http://boburbem.beget.tech/';

const options = {
    method: 'POST',
    'Content-Type': 'application/x-www-form-urlencoded',
};

data = "code='hellooo'"

let result = '';
const req = http.request(url, options, (res) => {
    console.log(res.statusCode);

    res.setEncoding('utf8');
    res.on('data', (chunk) => {
        result += chunk;
    });

    res.on('end', () => {
        console.log(result);
    });
});

req.on('error', (e) => {
    console.error(e);
});

req.write(data);
req.end();