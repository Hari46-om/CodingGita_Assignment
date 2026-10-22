// 1.

// let temp=[28,32,25,40,18,35]
// let count=0;
// for(let i=0;i<temp.length;i++){
//     if (temp[i]>30){
//         count+=1
//     }
// }
// console.log(count)

// 2.

// let num=4729;
// let digit=Math.floor(Math.log10(num))
// let sum=0;
// for(let i=0;i<=digit;i++){
//     sum+=num%10
//     num=Math.floor(num/10)
// }
// console.log(sum)

3.

// for(let i=1;i<=100;i++){
//     if(i%3===0 && i%5===0 && i%7!==0){
//         console.log(i)
//     }
// }

4.

// let str="JavaScript";
// let x="";
// for(let i=0;i<str.length;i++){
//     if(str[i]==="a" || str[i]==="e" || str[i]==="i" || str[i]==="o" || str[i]==="u"){

//     }else{
//         x+=str[i]
//     }
// }
// console.log(x)

5.

// let max=0;
// let num=[28, 32, 25, 40, 18, 35]
// for(let i=0;i<num.length;i++){
//     if(num[i]>max){
//         max=num[i]
//     }
// }
// console.log(max)

6.

// let num=28
// let sum=0;
// for(let i=0;i<num;i++){
//     if(num%i==0){
//         sum+=i
//     }
// }if(sum===num){
//     console.log("its perfect number")
// }else{
//     console.log("its not a perfect number")
// }

7.

// let sum=1;
// let series=7
// console.log("1")
// for(let i=0;i<series;i++){
//     sum+=sum
//     console.log(sum)
// }

8.


// let a=0;
// let b=1;
// let fib_series="0  1  ";
// for(let i=1;i<=18;i++){
//     let c=a+b
//     fib_series += c + "  "
//     a=b
//     b=c
// }
// console.log(fib_series)

9.

// let num=[45, 78, 90, 32, 56, 88]
// let sum=0
// let count=0
// for(let i=0;i<num.length;i++){
//     sum+=num[i]
// }
// let avg=sum/num.length
// for(let i=0;i<num.length;i++){
//     if(num[i]>avg){
//         count+=1
//     }
// }
// console.log(avg,count)

10.

// let num=49;
// let binary=""
// for(let i=1; num!=0;i++){
//     let remainder = num%2
//     binary += remainder
//     num = Math.floor(num/2)
// }
// console.log(binary)
// let rev=""
// for(let i=binary.length-1;i>=0;i--){
//     rev += binary[i]
// }
// console.log(rev)

// let num=49;
// let binary=""
// for(let i=1; num!=0;i++){
//     let remainder = num%2
//     binary = remainder + binary
//     num = Math.floor(num/2)
// }
// console.log(binary)

