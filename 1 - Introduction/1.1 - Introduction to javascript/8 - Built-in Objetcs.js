// There are more objets that you can use in JavaScript other than the console.
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects

// For example, if you want perform complicated mathematical operations, JavaScript has the Math object
// You can use the .random to get a random number
console.log(Math.random()); // Prints a number between 0 and 1

// If you want to get a random number from a different of numbers
// You can multiplicate the  operator
console.log(Math.random() * 69); // Returns a random number between 0 and 69

// The example above will probable won't return you a hole number, so to fix that you use the Math.floor() object to get the nearest hole number
console.log(Math.floor(Math.random() * 69));
