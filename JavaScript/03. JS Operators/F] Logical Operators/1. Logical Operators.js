1.

let username="admin"
let password="1234"
let userInput="admin"
let userPassword="1234"
if(username === userInput && password === userPassword ){
    console.log("Logged In")
}
else{
    console.log("Wrong Password")
}

2.

let isLoggedIn=true
let hasPassword=true
if(isLoggedIn && hasPassword){
    console.log("permission applied")
}
else{
    console.log("permission denied")
}

3.

let isStock = true;
let price=800;
if(isStock && price<1000){
    console.log("it can bought")
}
else{
    console.log("it can not bought")
}

4.

let marks=75;
let attendance=80;
if(marks>65 && attendance>70){
    console.log("student has passed")
}
else{
    console.log("student has failed")
}

5.

let isWeekend=true
let isHoliday=false
if(isHoliday===true && isWeekend===true){
    console.log("party will happens")
}
else{
    console.log("party cancled")
}

6.

// // Predict the output:
//    let a = 0;
//    let b = 10;
//    let result = a && b;
//    console.log(result);       //false && true ==> false(0)

// // 7.

// // // Predict the output:
// //    let x = 5;
// //    let y = 10;
// //    let result = (x > 3 && y) || 0;
// //    console.log(result);                  //5>3 && 10 ==> true && true ==>true(10) || 0 ==>true(10)

// 8.

// // Predict the output:
   let p = "Hello";
   let q = "";
   let r = "World";
   let result = p && q && r;
   console.log(result);              //"hello"(true) && ""(false) && "world"(true)  ==>false("")

// 9.

// // Predict the output:
//    let val = 5;
//    let condition = val && (val = 0);
//    console.log(condition);                 //true && false ==>false(0)
//    console.log(val);                       //0


10.

// //  Predict the output:
//     let x = 10;
//     let y = 20;
//     let result = (x && y) && (x > y);
//     console.log(result);                 //20 && false ==> false
