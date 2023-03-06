const fs = require('fs');
// content = "password()"
// fs.writeFile('need.txt', content, { flag: 'w+' }, err => {});


fs.readFile('answer.txt', 'utf8', (err, data) => {
    var c = "data"
    console.log(data);
})


console.log("success");