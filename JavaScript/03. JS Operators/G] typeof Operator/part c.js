11.

console.log(typeof typeof 100);                 //string
console.log(typeof typeof "Hi");                //string
console.log(typeof typeof true);                //string

12.

let a = 10;
let b = "10";
console.log(typeof a === typeof b);             //false
console.log(typeof a == typeof b);              //false

13.
 
console.log(typeof null === "object");          //true
console.log(typeof [] === "object");            //true
console.log(typeof {} === "object");            //true

14.

let x;
console.log(typeof x);                           //undefined
x = null;
console.log(typeof x);                           //object
x = 0;
console.log(typeof x);                           //number

15.

console.log(typeof NaN === "number");               //true
console.log(typeof Infinity === "number");          //true
console.log(typeof (1 / 0));                        //number