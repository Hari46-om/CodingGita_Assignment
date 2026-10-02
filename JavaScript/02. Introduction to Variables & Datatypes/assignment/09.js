// 09: Predict and Explain

var x = 10;

if (true) {
var x = 20;
let y = 30;
const z = 40;
}

console.log(x); // 20
// console.log(y); // ReferenceError
// console.log(z); // ReferenceError