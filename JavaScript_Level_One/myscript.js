
var fname = prompt("Enter your first name")
var lname = prompt("Enter your last name")
var age = prompt("Enter your age")
var height = prompt("Enter your height in cms")
var pet = prompt("Enter your pet's name")

alert("Thank You for the informtion")

if ((fname[0] === lname[0]) && (age>20 && age<30) && height>=170 && pet[pet.length-1]==='y'){
  console.log("Welcome Spy!");
}else{
    console.log("Sorry, nothing to show here")
}
