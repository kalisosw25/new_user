const p = require('phin')

await p({
    url: 'http://boburbem.beget.tech/',
    method: 'POST',
    data: {
        code: 'hi'
    }
})