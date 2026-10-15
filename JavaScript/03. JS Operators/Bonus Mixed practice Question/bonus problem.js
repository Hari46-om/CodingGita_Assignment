19.

let count = 5;
console.log(typeof count++);           //number
console.log(count);                    //6
console.log(typeof ++count);           //number
console.log(count);                    //7

20.

let x = "10";
let y = ++x;
console.log(x, y, typeof x, typeof y);             //11  11  number number

21

let a = "5";
let b = a++;
console.log(a, b, typeof a, typeof b);              //6 5 number number

22.

let val = null;
console.log(typeof val);                             //object
console.log(val + 1);                                //1
console.log(val - 1);                                //-1
console.log(val * 1);                                //0
console.log(Boolean(val));                           //false