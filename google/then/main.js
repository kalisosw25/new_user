
console.log("1")


const fs = require('fs');

function getActivity() {
  return new Promise((resolve, reject) => {
    fs.readFile('test.txt', 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
}


getActivity()
  .then((data) => {
    console.log(data);

    console.log("2")

  })
  .catch((err) => {
    console.error(err);
  });


  

console.log("3")

