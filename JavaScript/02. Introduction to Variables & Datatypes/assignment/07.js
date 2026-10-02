// 07: Test Re-declaration

var user = "Alice";
var user = "Bob";

console.log(user);

// let does not allow re-declaration in the same scope.
// Uncommenting the next two lines causes a SyntaxError.
//
// let student = "Alice";
// let student = "Bob";