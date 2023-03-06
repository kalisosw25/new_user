const { PythonShell } = require("python-shell");
let options = {
    mode: 'text',
    pythonPath: 'path/to/python',
    pythonOptions: ['-u'], // get print results in real-time
    scriptPath: 'path/to/my/scripts',
    args: ['value1', 'value2', 'value3']
  };
PythonShell.runString('x=1+1;print(x)', options).then(messages=>{
    console.log('results: %j', results);
});

console.log("--------")
// node m.js