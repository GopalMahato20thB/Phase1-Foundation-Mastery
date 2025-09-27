console.log("Building Javascript Objects");

var ourDog = {
	"name": "Jony",
	"legs": 4, 
	"tails": 2,
	"friends": ["Everything!"]
};

console.log(ourDog);

var friends_info = {
	"names": ["Ujjwal", "Manaranjan"], 
	"age": [19, 19],
	"city": "Balarampur",
	"Is_friend": true
}

console.log("Friends ", friends_info.names);

// Accessing Object Properties with Bracket Notation

var fav_things = {
	"Name": "Gopal",
	"Food": "Dhal Bhat", 
	"Sports": "Watching PL",
	"Favorite Club": "Manchester City"
}

console.log("Favorite Club: ", fav_things["Favorite Club"])

// Update object property

fav_things.Name = "Gopal Mahato";
console.log(fav_things);

// Add New Properties to an Object

fav_things.skills = "Basic python, javascript, C, C++";

console.log(fav_things);

// delete Properties From an Object
// We need to use delete keyword
// Before that i will add somethings then i wil delete that 
fav_things.videos = "Killer";
console.log(fav_things);

delete fav_things.videos;

console.log(fav_things);









