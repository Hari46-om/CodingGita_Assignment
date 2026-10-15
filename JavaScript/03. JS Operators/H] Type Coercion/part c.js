11.

// console.log("5" + 3 + 2);          //532
// console.log(5 + 3 + "2");          //82
// console.log("5" - 3 + 2);          //4
// console.log(5 - "3" + "2");        //22

12.

// console.log(true + true);           //2
// console.log(true + false);          //1
// console.log(true + "false");        //truefalse  
// console.log(false + "true");        //falsetrue

// 13.

// console.log(null + 5);              //5
// console.log(undefined + 5);         //NaN
// console.log(null + "5");            //null5
// console.log(undefined + "5");       //undefined5

14.

// console.log([] + []);                //
// console.log([] + {});                //[object Object]
// console.log({} + []);                //[object Object]
// console.log({} + {});                //[object Object][object Object]

// 15.

// let a = "10";
// let b = 5;
// let c = a + b;
// let d = a - b;
// let e = +a + b; 
// console.log(c, typeof c);                 //105 string
// console.log(d, typeof d);                 //5 number
// console.log(e, typeof e);                 //15 number

16.

console.log(!!"Hello");                   //true
console.log(!!"");                        //false
console.log(!!0);                         //false
console.log(!!1);                         //true
console.log(!!null);                      //false
console.log(!!undefined);                 //false

17.

console.log(Number(""));                   //0
console.log(Number(" "));                  //0
console.log(Number("0"));                  //0
console.log(Number("  25  "));             //25
console.log(Number("25px"));               //NaN

18.

let val1 = "5";
let val2 = 2;
console.log(val1 + val2);                   //52
console.log(+val1 + val2);                  //7
console.log(val1 - val2);                   //3
console.log(val1 * val2);                   // 10                  
console.log(val1 / val2);                   //2.5