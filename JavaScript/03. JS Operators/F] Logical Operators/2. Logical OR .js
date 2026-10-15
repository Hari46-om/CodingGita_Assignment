1.

let passwordCorrect = true
let otpValid = false
console.log("user can login :", passwordCorrect || otpValid)

2.

let isMember=false
let hasCoupon=true
console.log("discount applies",isMember||hasCoupon)

3.

let age =16
let height=155
if(age>18 || height>150){
    console.log("Entery is allowed")
}
else{
    console.log("Entery is not allowed")
}

4.

let  emailGiven=true
let phoneGiven=false
console.log("a form is valid", emailGiven || phoneGiven)

5.

let score=900
let timeBouns=true
if(score>1000 || timeBouns===true){
    console.log("Game level is open")
}
else{
    console.log("game level is not open")
}

6.

// Predict the output:
   let a = 0;
   let b = false;
   let c = "";
   let d = null;
   let e = 42;
   let result = a || b || c || d || e;
   console.log(result);                  //true(42)

7.

// Predict the output:
//    let x = "Hello" || 0;
//    let y = 0 || "Hi";
//    console.log(x, y);                     //Hello,Hi


8.

// // Predict the output:
//    let a = 10;
//    let b = 20;
//    let result = (a < 5) || (b > 15);
//    console.log(result);                    // false||true===> true

9.

// Predict the output:
   let val = 5;
   let condition = val || (val = 0);
   console.log(condition);                      //true(5)
   console.log(val);                            //0

10.

// Predict the output:
    let x = "" || 0 || false || null || undefined || "OK";
    console.log(x);                                       // OK