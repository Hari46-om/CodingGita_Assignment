1.

let month=2

switch (month){
    case 1:
        console.log("31 days in January")
        break;
    case 2:
        console.log("28 days in February")
        break;
    case 3:
        console.log("31 days in march")
        break;
    case 4:
        console.log("30 days in April")
        break;
    case 5:
        console.log("31 days in May")
        break;
    case 6:
        console.log("30 days in June")
        break;
    case 7:
        console.log("31 days in July")
        break;
    case 8:
        console.log("31 days in August")
        break;
    case 9:
        console.log("30 days in september")
        break;
    case 10:
        console.log("31 days in Octuber")
        break;
    case 11:
        console.log("30 days in November")
        break;
    case 12:
        console.log("31 days in December")
        break;
    default:
        console.log("Invalid month number")
}

// 2.

// let chr="a"

// switch (true){
//     case chr=="a" || chr=="e" || chr=="i" || chr=="o" || chr=="u" :
//         console.log("Vowel")
//         break
//     case chr=="A" || chr=="E" || chr=="I" || chr=="O" || chr=="U" :
//         console.log("Vowel")
//         break
//     default:
//         console.log("consonaNT")
// }

// // 3.

// // let seasonNum=2;

// // switch(true){
// //     case seasonNum==1 || seasonNum==2:
// //         console.log("winter")
// //         break;
// //     case seasonNum==3 || seasonNum==4:
// //         console.log("Summer")
// //         break;
// //     default:
// //         console.log("Invalid Number")
// // }

// // //-------------------------------or-----------------------------------


// // let seasonNum=2;

// // switch(seasonNum){
// //     case 1: case 2:
// //         console.log("winter")
// //         break;
// //     case 3: case 4:
// //         console.log("Summer")
// //         break;
// //     default:
// //         console.log("Invalid Number")
// // }


// 4.

// let mark=85;

// switch(true){
//     case mark>=75 && mark<=100:
//         console.log("Distinction")
//         break;
//     case mark>=60 && mark<=74:
//         console.log("1st class")
//         break;
//     case mark>=50 && mark<=59:
//         console.log("2nd class")
//         break;
//     case mark>=35 && mark<=49:
//         console.log("3rd class")
//         break;
//     case mark<=34:
//         console.log("Failed")
//         break;
//     default:
//         console.log("Invalid marks")
// }


5.

let role="admin";
let action="create";

switch(role){
    case "admin":
        switch(action){
            case "create":
                console.log("can create")
                break;
            case "edit":
                console.log("can edit")
                break;
            case "delete":
                console.log("delete")
                break;
        }
        break;
    case "user":
        console.log("limited Access")
        break;
}

6.

// outup:mango is red 
//       Banana is yellow
//       unknown fruit 
//       because break is not use this code will not stop

let fruit = "mango";

switch (fruit) {
  case "apple":
    console.log("Apple is red");
    break;
  case "mango":
    console.log("Mango is yellow");
    break;
  case "banana":
    console.log("Banana is yellow");
    break;
  default:
    console.log("Unknown fruit");
    break;
}

7.

let value=null

switch(true){
    case value===0:
        console.log("number")
        break;
    case value==="0":
        console.log("string")
        break;
    case value===false:
        console.log("Boolean")
        break;
    case value===null:
        console.log("null value")
        break;
    case value===undefined:
        console.log("number")
        break;
    default:
        console.log("invalid")
}

8.

let a=10
let b=2
let operater="**"

switch(operater){
    case "+":
        console.log(a+b)
        break;
    case "-":
        console.log(a-b)
        break;
    case "*":
        console.log(a*b)
        break;
    case "/":
        console.log(a/b)
        break;
    case "%":
        console.log(a%b)
        break;   
    case "**":
        console.log(a**b)
        break;  
    default:
        console.log("unvalid operator")   
}

9.

let day=25;
switch(day){
    case day>=1 && day<=10:
        console.log("Beginning of the month")
        break;
    case day>=11 && day<=20:
        console.log("Middle of the month")
        break;
    case day>=21 && day<=31:
        console.log("End of the month")
        break;
    default:
        console.log("invalid day")

}

10.

let category = "veg";
let item = "paneer";
let size = "half";

switch (category) {
    case "veg":
        switch (item) {
            case "paneer":
                switch (size) {
                    case "half":
                        console.log("Order: Veg Paneer, Half, ₹150");
                        break;
                    case "full":
                        console.log("Order: Veg Paneer, Full, ₹300");
                        break;
                    default:
                        console.log("Invalid size");
                }
                break;

            default:
                console.log("Invalid veg item");
        }
        break;

    case "nonveg":
        switch (item) {
            case "chicken":
                switch (size) {
                    case "half":
                        console.log("Order: Chicken, Half, ₹200");
                        break;
                    case "full":
                        console.log("Order: Chicken, Full, ₹400");
                        break;
                    default:
                        console.log("Invalid size");
                }
                break;

            default:
                console.log("Invalid nonveg item");
        }
        break;

    default:
        console.log("Invalid category");
}