1.

// let num=35;
// let result=num%7==0? "divisible by 7": "not divisible by 7"
// console.log(result)

2.

// let temp=25;
// let result=temp>=30? "Hot Day": "Pleasant Day"
// console.log(result)

3.

// let x=""
// let result=x==""? "Empty string" : "string has content"
// console.log(result)

4.

// let age=5;
// let result=age<13?"child": age>=13 && age<=19? "teenager":"Adult"
// console.log(result)

5.

// let num1=500
// let num=89
// let num2=6532
// let result=num>num1 && num>num2? `${num} is greater`:num1>num && num1>num2? `${num1} is greater`:`${num2} is greater`
// console.log(result)

6.

// let mark=85;
// let result=mark>=75 && mark<=100?"Distinction":mark>=60 && mark<=74?"1st class":mark>=50 && mark<=59?"2nd class":mark>=35 && mark<=49?"pass":mark<=34 ?"Fail":"invalid marks"
// console.log(result)

7.

// let num=-6165
// let result=num>0?(num%2==0?"postivie and even": "Positive and odd"): num<0?(num%2==0?"negative and even":"negative and odd"):"zero";
// console.log(result)

8.

// let year=2024
// let result=year%4==0?(year%100==0? (year%100==0?"leap year and century":"not a leap year"):"leap year"):"not a leap year"
// console.log(result)

9.

// let role="admin"
// let action="delete"
// let result=role ==="admin"?(action === "delete"?"Admin Delete":action === "edit"?"Admin Edit":"Admin Other"):role === "user"?(action === "view"?"User View":"User Restricted"):"Invalid Role";
// console.log(result)


10.

let cartTotal=6000
let result=cartTotal>=5000? `final amount${cartTotal-cartTotal*0.20}`:cartTotal>=2000?`final amount${cartTotal-cartTotal*0.10}`:cartTotal>=1000?`final amount${cartTotal-cartTotal*0.05}`: `final amount${cartTotal}`
console.log(result)