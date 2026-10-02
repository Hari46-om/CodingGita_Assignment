// 08: Test Re-assignment

var a = 10;
let b = 20;
const c = 30;

a = 100;
b = 200;

// c = 300; // TypeError: Assignment to constant variable.

console.log(a);
console.log(b);
console.log(c);