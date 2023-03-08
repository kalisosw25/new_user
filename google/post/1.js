const { response } = require('express');
const http = require('http');

http.get('http://boburbem.beget.tech/' , (response) => {
    let data = '';
    response.on('data' , (chunk) => {
        data += chunk;
    })

    response.on('end', () => {
        console.log(data)
    })
})
.on('error' , (error) => {
    console.log(error)
})


console.log("hi---------")