const { spawn } = require('child_process');

// define the Python script and arguments
const pythonScript = 'my_script.py';
const args = ['arg1', 'arg2', 'arg3'];

// execute the Python script as a child process
const pythonProcess = spawn('python', [pythonScript, ...args]);

// listen for output from the Python process
pythonProcess.stdout.on('data', (data) => {
  console.log(`Python script output: ${data}`);
});

// listen for errors from the Python process
pythonProcess.stderr.on('data', (data) => {
  console.error(`Python script error: ${data}`);
});

// listen for the Python process to exit
pythonProcess.on('close', (code) => {
  console.log(`Python script exited with code ${code}`);
});

while (1<100) {
    console.log('Python')
}



console.log("hello--------------------------")