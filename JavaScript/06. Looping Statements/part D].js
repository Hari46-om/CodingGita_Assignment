1.
// for (let i = 50; i>=1; i--){
//     if (i%3==0 && i%9!=0){
//         console.log(i);
//     }
// }


2.
// let num = 4729
// let product = 1
// for (let i = toString(num).length; i>=1; i--){
//     if ((num%10)%2!=0){
//         product *= num%10
//     }
//     num = Math.floor(num/10)
// }
// console.log(product);


3.
// let string = "Programming"
// let newString = ""
// for (let i = string.length-1; i>=0; i--){
//     char = string[i]
//     if (!"aeiouAEIOU".includes(char)){
//         newString+=char
//     }
// }
// console.log(newString);


4.
// let val2 = 377
// let val1 = 233
// let numbers = ""
// numbers += val2 + " " + val1 + " "
// for (let i=15; i>2; i--){
//     let val3 = val2 - val1
//     numbers += val3 + " "
//     val2 = val1
//     val1 = val3
// }
// console.log(numbers);


5.
// let number = 47974
// let numberCopy = number
// let numberReverse = 0
// for (let i=1; i<=Math.ceil(Math.log10(number)); i++){
//     numberReverse = numberReverse*10 + numberCopy%10
//     numberCopy = Math.floor(numberCopy/10)
// }
// if (number == numberReverse){
//     console.log("Palindrome");
// }else {
//     console.log("Not a Palindrome");
// }


6.
// let nums = [12, 45, 7, 23, 56, 89, 34]
// let largestNum = 0
// for (let i = nums.length-1; i>=0; i--){
//     if (nums[i]>largestNum && nums[i]<50){
//         largestNum=nums[i]
//     }
// }
// console.log(largestNum);


7.
// let temps = [32, 28, 41, 19, 35, 27, 38]
// let count = 0
// for (let i = temps.length-1; i>=0; i--){
//     if (temps[i]<30){
//         count+=1
//     }
// }
// console.log(count);


8.
// let number = 13
// let binary = ""
// for (let i = 0; i<= 20; i++){
//     binary += number%2
//     number = Math.floor(number/2)
//     if (number==0){
//         break
//     }
// }
// let binaryReverse = ""
// for (let i = binary.length-1; i>=0; i--){
//     binaryReverse+=binary[i]
// }
// console.log(binaryReverse);


9.
// let scores = [90, 85, 70, 95, 60, 88, 75]
// for (let i = scores.length-1; i>=0; i--){
//     if (scores[i]>80){
//         console.log(`Score: ${scores[i]}, Index: ${i}`);
//         break
//     }
// }


10.
// for (let i=40; i>=1; i--){
//     if (i**0.5%1==0){
//         continue
//     }
//     console.log(i);
// }