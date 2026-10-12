11.

let x = 10;                 //12
let y = x++;                //10
let z = ++x;                //12
console.log(x, y, z);

output:12,10,12

12.

let a = 5;                //5
let b = a-- + ++a;        //10
console.log(a, b);  

output:5,10

13.

let m = 7;               //7
let n = --m + m++;       //12
console.log(m, n);

output:7,12

14.

let p = 3;                    //5
let q = p++ + ++p + p;        //13
console.log(p, q);

output:5,13

15.

let val = 0;            
val = val++ + ++val;     //2
console.log(val);

output:2