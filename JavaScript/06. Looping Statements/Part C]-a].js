1.

// let arr=[10,45,7,5,8,85,65]
// for(let i=0;i<arr.length;i++){
//     if( arr[i]==7){
//         console.log(i)
//         break
//     }
// }

2.

// let correctPassword = "1234@correct"
// let enteredPassword = "1234@incorrect"
// attempt = 1
// for (let i = 1; i <= 5; i++) {
//     console.log("Enter Password: ");
//     if (correctPassword == enteredPassword) {
//         console.log("Access granted");
//         break
//     } else if (attempt == 5) {
//         console.log("Account locked");
//         break
//     }
//     attempt += 1
// }

let Password=1234
let flag=false
for(let i=1;i<=5;i++){
    let enteredPassword=prompt("enter the Password :");
    if(parseInt(enteredPassword)===Password){
        console.log("Access granted");
        flag = true
        break
    }
}
if(flag==false){
    console.log("account locked") 
}


3.


// let total = 0
// for (let i = 1; i <= 100; i++) {
//     total += i
//     if (total > 100) {
//         console.log(i);
//         break
//     }
// }


4.


// let names = ["Fsd", "Asdas", "Sadeds", "Syrameof"]
// for (let i = 0; i < names.length; i++) {
//     if (names[i].startsWith("S", 0)) {
//         console.log(names[i]);
//         break
//     }
// }

5.


// for (let i = 1; i <= 50; i++) {
//     if (i > 20 && (i ** 0.5) % 1 == 0) {
//         break
//     }
//     console.log(i);
// }