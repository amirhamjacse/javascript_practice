let count = 1;
const name = "Hamja";
count += 1; 

const add = (a, b)=> a+b;
const squre = x => x*x;
const message = `My name is ${name}`


console.log(count, name ,add(1,2), squre(3), message);


const user = {
    name: "hamja",
    age: 25
};

const {name, age} = user
console.log(name, age)

const arr = [1,2,3,4]
const [first, second] = arr
console.log(first, second)

Sum any number of numbers
const sum = (...numbers) => {
    return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(1,2,3));       // 6
console.log(sum(10,20,30,40)); // 100

const age = 20;

if (age < 18){
    consol.log("child");
}
else if (age > 30){
    consol.log("Young adult")
} else {
    console.log("Adult")
}


const num = 10;

if (num >= 45){
    console.log("huge");
} else if (num >=4){
    console.log("Good number")
} else {
    console.log("Very nice")
}

for(let i=0; i<5; i++){ console.log(i); }

for (let i=1; i<11; i++){console.log(i);}

const age = 34;
const status = age>= 23 ? "Adult" : "child";
console.log(status)


const numbers = [1,2,3,4,5];
numbers.forEach(n => console.log(n));
const squares = numbers.map(n => n*n);
const evens = numbers.filter(n => n%2===0);
const sum = numbers.reduce((a,b)=>a+b,0);



const fruits = ["apple", "banana", "orange"];

for (let i=0; i<fruits.length; i++){
    console.log(fruits[i]);
}

























