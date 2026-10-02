// 11: Predict the Hoisting Behavior

// var is hoisted and initialized with undefined.
console.log(a);

// let and const are in the Temporal Dead Zone here.
// console.log(b); // ReferenceError
// console.log(c); // ReferenceError

var a = 10;
let b = 20;
const c = 30;

console.log(b);
console.log(c);