let {PythonShell} = require('python-shell')
let options = {
    args:["aaa","bbb"]
}
PythonShell.run("function.py" , options , function (err, result){
    console.log(result.toString())
    res.send(result.toString())
    console.log("running")
    if (err) {
        console.log(err)
    }
    else{
        // console.log(logs)
        console.log(results.toString())
        console.log('finish')
    }
})


console.log('finish-------------')