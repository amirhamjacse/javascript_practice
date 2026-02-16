# **1. JavaScript Data Types**

### **Primitive Types**

| Type      | Example                 | Notes                   |
| --------- | ----------------------- | ----------------------- |
| String    | `"Hello"`, `'World'`    | Text                    |
| Number    | `10`, `3.14`            | Integers and floats     |
| Boolean   | `true`, `false`         | True/false values       |
| Null      | `null`                  | Empty value             |
| Undefined | `undefined`             | Not assigned            |
| Symbol    | `Symbol('id')`          | Unique identifier       |
| BigInt    | `12345678901234567890n` | For very large integers |

```javascript
let name = "Alice";
let age = 25;
let isActive = true;
let unknown = null;
let notDefined;
```

---

### **Reference Types**

| Type     | Example                    | Notes               |
| -------- | -------------------------- | ------------------- |
| Object   | `{name: "Alice", age: 25}` | Key-value pairs     |
| Array    | `[1, 2, 3, 4]`             | Ordered collection  |
| Function | `function greet(){}`       | Callable code block |
| Date     | `new Date()`               | Date & time         |
| RegExp   | `/abc/`                    | Regular expression  |

```javascript
const user = { name: "Alice", age: 25 };
const numbers = [1, 2, 3, 4];
const greet = () => console.log("Hello!");
```

---

# **2. Variables**

```javascript
var oldVar = "old";   // function-scoped, avoid
let count = 0;        // block-scoped, can change
const pi = 3.14;      // block-scoped, cannot change
```

---

# **3. Operators**

### **a) Arithmetic**

```javascript
let a = 10, b = 3;
console.log(a + b); // 13
console.log(a - b); // 7
console.log(a * b); // 30
console.log(a / b); // 3.3333
console.log(a % b); // 1 (remainder)
console.log(a ** b); // 1000 (power)
```

### **b) Assignment**

```javascript
let x = 5;
x += 2; // x = 7
x -= 1; // x = 6
x *= 2; // x = 12
x /= 3; // x = 4
```

### **c) Comparison**

```javascript
console.log(5 == '5');   // true (loose equality)
console.log(5 === '5');  // false (strict equality)
console.log(5 != 3);     // true
console.log(5 !== '5');  // true
console.log(5 > 3);      // true
console.log(5 <= 5);     // true
```

### **d) Logical**

```javascript
console.log(true && false); // false
console.log(true || false); // true
console.log(!true);         // false
```

---

# **4. Conditional Statements**

### **if / else if / else**

```javascript
let age = 20;

if(age < 18){
  console.log("Child");
} else if(age < 30){
  console.log("Young Adult");
} else {
  console.log("Adult");
}
```

### **Ternary Operator**

```javascript
let status = age >= 18 ? "Adult" : "Child";
console.log(status);
```

### **Switch Statement**

```javascript
let day = 3;
switch(day){
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  case 3:
    console.log("Wednesday");
    break;
  default:
    console.log("Other day");
}
```

---

# **5. Loops**

### **For Loop**

```javascript
for(let i = 0; i < 5; i++){
  console.log(i);
}
```

### **While Loop**

```javascript
let i = 0;
while(i < 5){
  console.log(i);
  i++;
}
```

### **Do-While Loop**

```javascript
let j = 0;
do {
  console.log(j);
  j++;
} while(j < 5);
```

### **For…of (Arrays)**

```javascript
const fruits = ["apple", "banana", "orange"];
for(const fruit of fruits){
  console.log(fruit);
}
```

### **For…in (Objects)**

```javascript
const user = {name: "Alice", age: 25};
for(const key in user){
  console.log(key, user[key]);
}
```

---

# **6. Functions**

### **Traditional Function**

```javascript
function greet(name){
  return `Hello, ${name}`;
}
console.log(greet("Alice"));
```

### **Arrow Function**

```javascript
const greet = name => `Hello, ${name}`;
console.log(greet("Bob"));
```

### **Function with Default Parameters**

```javascript
const greet = (name = "Guest") => `Hello, ${name}`;
console.log(greet()); // Hello, Guest
```

---

# **7. Arrays**

```javascript
const numbers = [1, 2, 3, 4, 5];

// Methods
numbers.push(6);       // add to end
numbers.pop();         // remove last
numbers.shift();       // remove first
numbers.unshift(0);    // add to start

// Iterate
numbers.forEach(n => console.log(n));
const squares = numbers.map(n => n*n);
const evens = numbers.filter(n => n % 2 === 0);
const sum = numbers.reduce((a,b) => a+b, 0);
```

---

# **8. Objects**

```javascript
const user = {
  name: "Alice",
  age: 25,
  greet: function(){
    console.log(`Hi, I am ${this.name}`);
  }
};

console.log(user.name);    // Alice
user.greet();              // Hi, I am Alice

// Object destructuring
const {name, age} = user;
console.log(name, age);
```

---

# **9. ES6+ Useful Features**

### **a) Template Literals**

```javascript
console.log(`My name is ${name} and I am ${age} years old`);
```

### **b) Spread & Rest**

```javascript
const arr1 = [1,2,3];
const arr2 = [...arr1, 4,5];
console.log(arr2); // [1,2,3,4,5]

function sum(...numbers){
  return numbers.reduce((a,b)=>a+b, 0);
}
console.log(sum(1,2,3)); // 6
```

### **c) Destructuring**

```javascript
const user = {name: "Alice", age: 25};
const {name, age} = user;
console.log(name, age);
```

### **d) Modules**

```javascript
// export.js
export const greet = name => `Hello ${name}`;

// import.js
import { greet } from './export.js';
console.log(greet("Alice"));
```

---

# **10. Modern JS Tips for Vue & Next**

1. **Always use `const` for components, functions, arrays, objects if not reassigned**
2. **Use arrow functions for callbacks but not for Vue `methods`**
3. **Use destructuring for props in Vue/Next**
4. **Async/await for API calls**
5. **Template literals for dynamic HTML or JSX content**

