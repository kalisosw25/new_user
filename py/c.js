const util = require('util');
const exec = util.promisify(require('child_process').exec);
    
function runPythonFile() {
  console.log("stdout")
  const { stdout, stderr } = exec('python3 script.py -s asdf -d pqrs');
  if (stdout) { console.log("stdout") }
  if (stderr) { console.log("stderr") }
}
runPythonFile()
console.log("data=======================")