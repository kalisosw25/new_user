function python_function(something){
  const { spawn } = require('child_process');
  const pyScript = spawn('python', ['function.py' , something]);
  var something_print ;
  pyScript.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
    something_print = data ;
    return data ;
  });
  // console.log(something_print)
  
  pyScript.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  
  pyScript.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
  return something_print
}
function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}
console.log("---------------------------")

a = python_function("random_password")
console.log(a)
sleep(5000)
console.log("---------------------------")