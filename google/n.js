function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms);
    });
  }


py_function = async (what) => {
  console.log()
  const { PythonShell } = require("python-shell");
  let pyshell = new PythonShell("my_script.py");
  await pyshell.send(what);
  const sss = ["Banana"];
  await pyshell.on("message", function (message) {
    console.log(message);
    sss.push(message);
  });
  // setTimeout(() => {
  //   pyshell.send("Another Hello");
  // }, 3000);
  const end = () => {
    pyshell.end(function (err, code, signal) {
      if (err) throw err;
      //   console.log("finished");
      //   console.log(sss);
      //   console.log("--------------------------")
      return sss
    });
  };
  end();

  //   return sss
}
py_function("password");

sleep(10000)
// cc = py_function("password")
console.log("{aaa}")
console.log("-------------------------")


// node n.js