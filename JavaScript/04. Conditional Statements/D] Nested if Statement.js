1.

let num=15
if(num>10){
    if(num%3==0){
        console.log("The number is greater than 10 and divisible by 3");
    }else{
        console.log("The number is greater than 10 but not divisible by 3");
    }
}

2.

let age=19
let hasVoterId=true
if(age>=18){
    if(hasVoterId){
        console.log("eligible to vote");
    }
}

3.

let marks=75
if(marks>=40){
    if(marks>=80){
        console.log("distinction");
    }else{
        console.log("passed");
    }
}

4.

let pin=1234
let balance=1000
if(pin==1234){
    if(balance>=500){
        console.log("sufficient balance for withdrawal");
    }else{
        console.log("insufficient balance for withdrawal");
    }
}

5.

let year=2024
if(year%4==0){
    if(year%100==0){
        if(year%400==0){
            console.log("leap year");
        }else{
            console.log("not a leap year");
        }
    }else{
        console.log("leap year");
    }
}

6.

let email="abc.cg@gmail.com";

if(email.includes('@')==true){
    console.log("yes")
    let l = email.length;
    let last_chars =email[1-4]+email[l-3]+email[l-2]+email[l-1]
    if (last_chars==".com"){
        if(l>10){
            console.log(`the email ${email} is valid Email`)
        }
    }
}

7.

let cartTotal =1001;
let isPrimeMember=true;

if (cartTotal>=1000){
    if(isPrimeMember==true){
        cartTotal=cartTotal-(cartTotal*0.20)
    }else{
        cartTotal=cartTotal-(cartTotal*0.10)
    }
}

console.log(cartTotal)

8.

let num2=24
if(num2>0){
    if(num2%2==0){
        if(num2%4){
            console.log("Positive Even and Divisible by 4")
        }
    }
}

9.

let age1=54
let hasGraduationDegree=true
let experience=3
if (age1>=21 && age1<=30){
    if(hasGraduationDegree==true){
        if(experience>=2){
            console.log("Eligible for Interview” only if all three conditions are true.")
        }
    }
}

10.

let isPresent=true
let internalmark=35
let externalmark=45
if(isPresent==true){
    if(internalmark>=30){
        if(externalmark>=35){
            console.log("Eligible for Final Exam")
        }
    }
}

