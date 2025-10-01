/*
What is an Object?
An Object in Javascript is a collection of key-value pairs.
>>> Keys are called properties (or methods if they hold a function).
>>> Values can be anything: numbers, strings, arrays, other objects, or functions

*/


const person = {
  name : "Gopal Mahato", // property
  age : 20,             // property 
  walk: function(){     // method 
    console.log("I am walking... on the path!");
  },
  talk(){
    console.log("I am currently talking to myself in my mind!");
  }
}

console.log(person.name);
person.talk();

