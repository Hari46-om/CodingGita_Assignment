// Question 5: Symbol Uniqueness

let symbol1 = Symbol("id");
let symbol2 = Symbol("id");

console.log(symbol1 === symbol2);

const studentData = {
    [symbol1]: 123,
    [symbol2]: "Ritik"
};

console.log(studentData[symbol1]);
console.log(studentData[symbol2]);