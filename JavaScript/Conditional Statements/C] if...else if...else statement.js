1.

let month=2
if(month==1 && month==2 && month==12 ){
    console.log("Winter")
}else if(month==3 && month==4 && month==5){
    console.log("Summer")
}else if(month==6 && month==7 && month==8){
    console.log("Monsoon")
}else if (month==9 && month==10 && month==11){
    console.log("Autumn")
}else{
    console.log("invalid number")
}

2.

let income=5_00_000
if(income < 3_00_000){
    console.log("No tax")
}else if(income >= 3_00_000 && income < 7_00_000){
    console.log("5% tax")
}else if(income >= 7_00_000 && income < 10_00_000){
    console.log("10% tax")
}else if (income >= 10_00_000){
    console.log("15% tax")
}

3.

let marks=85
if(marks>=90){
    console.log("Outstanding")
}else if(marks>=70 && marks<89){
    console.log("Good")
}else if(marks>=40 && marks<69){
    console.log("Average")
}else if(marks<40){
    console.log("Need Improvement")
}

4.

let speed=34
if(speed>80){
    console.log("Fast")
}else if(speed>=40 && speed<=75){
    console.log("Normal")
}else{
    console.log("Slow")
}

5.

let height=154
if (height>170){
    console.log("Tall")
}else if(height>=150 && height<=170){
    console.log("Average")
}else{
    console.log("Short")
}

6.

let day=5
if(day>=1 && day<=5){
    console.log("Weekday")
}else if(day==6 || day==7){
    console.log("Weekend")
}else{
    console.log("Invalid day")
}

7.

let units=150
if (units>=150){
    console.log("total bill:",units*6)
}else if(units>=51 && units<150){
    console.log("total bill:",units*4)
}else if(units>=0 && units<50){
    console.log("total bill:",units*2)
}else{
    console.log("Invalid units")
}

8.

let attendance=75
if(attendance>=90){
    console.log("Excellent")
}else if(attendance>=75 && attendance<89){
    console.log("Good")
}else if (attendance>=50 && attendance<74){
    console.log("Satisfactory")
}else{
    console.log("Poor")
}

9.

let mark1=85
let mark2=90
let mark3=78
if (mark1>mark2 && mark1>mark3){
    console.log("mark1 is highest")
}else if (mark2>mark1 && mark2>mark3){
    console.log("mark2 is highest")
}else{
    console.log("mark3 is highest")
}

10.

let num=5
if(num>0){
    if(num%2==0){
        console.log("positive and even")
    }else{
        console.log("positive and odd")
    }
}else if(num<0){
    if(num%2==0){
        console.log("negative and even")
    }else{
        console.log("negative and odd")
    }
}else{
    console.log("zero")
}
