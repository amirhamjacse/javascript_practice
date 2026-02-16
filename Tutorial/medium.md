## **1. Modern JavaScript Essentials (ES6+)**

### **a) Let, Const, and Var**

* `let` → block-scoped variable
* `const` → block-scoped constant (cannot reassign)
* `var` → function-scoped (old, avoid if possible)

```javascript
let count = 0;
const name = "John";

count += 1; // ✅
name = "Doe"; // ❌ Error
```

> Both Vue and React prefer `let` and `const`—especially `const` for functions and components.

---

### **b) Arrow Functions**

* Shorter syntax, lexically binds `this` (important in Vue/React methods)

```javascript
const add = (a, b) => a + b;
const square = x => x * x;

console.log(add(2, 3)); // 5
```

> In Vue, arrow functions are **not suitable** as methods in `methods` because they bind `this` differently.

---

### **c) Template Literals**

* For dynamic strings

```javascript
const user = "Alice";
const message = `Hello, ${user}! Welcome to Vue/Next.js.`;
console.log(message);
```

---

### **d) Destructuring**

* Extract properties from objects or arrays

```javascript
const user = { name: "Alice", age: 25 };
const { name, age } = user; // object destructuring
console.log(name, age); // Alice 25

const arr = [1, 2, 3];
const [first, second] = arr; // array destructuring
console.log(first, second); // 1 2
```

> Useful in Next.js when receiving props or API responses.

---

### **e) Default Parameters**

```javascript
function greet(name = "Guest") {
  console.log(`Hello, ${name}!`);
}
greet(); // Hello, Guest!
```

---

### **f) Spread & Rest Operators**

* Spread (`...`) → expand iterable
* Rest (`...`) → collect remaining items

```javascript
// Spread
const arr = [1, 2, 3];
const newArr = [...arr, 4, 5];
console.log(newArr); // [1,2,3,4,5]

// Rest
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}
console.log(sum(1,2,3,4)); // 10
```

---

### **g) Modules (import/export)**

* Used in Vue & Next.js

```javascript
// math.js
export const add = (a, b) => a + b;

// main.js
import { add } from './math';
console.log(add(2,3));
```

---

## **2. Asynchronous JavaScript**

### **a) Promises**

```javascript
fetch('https://api.example.com/data')
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

### **b) Async/Await**

```javascript
async function getData() {
  try {
    const res = await fetch('https://api.example.com/data');
    const data = await res.json();
    console.log(data);
  } catch(err) {
    console.error(err);
  }
}
getData();
```

> Essential in Next.js `getServerSideProps` or Vue `mounted()` lifecycle when calling APIs.

---

## **3. ES6 Classes**

* For objects or services

```javascript
class User {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  greet() {
    return `Hi, I am ${this.name}`;
  }
}

const alice = new User("Alice", 25);
console.log(alice.greet());
```

> Useful for utilities or data models in large projects.

---

## **4. Modern JavaScript in Vue.js**

### **a) Vue 3 Composition API**

* Uses modern JS features heavily

```javascript
import { ref, computed } from 'vue';

export default {
  setup() {
    const count = ref(0);
    const double = computed(() => count.value * 2);

    function increment() {
      count.value++;
    }

    return { count, double, increment };
  }
}
```

> Note: `ref` uses `.value` because it’s reactive. Arrow functions work here!

---

### **b) Reactive Objects**

```javascript
import { reactive } from 'vue';

const state = reactive({
  name: "Alice",
  age: 25
});

state.age++;
```

---

## **5. Modern JavaScript in Next.js**

### **a) Functional Components**

```javascript
function Home({ user }) {
  return <h1>Hello, {user.name}</h1>;
}

export default Home;
```

### **b) Fetching Data**

```javascript
export async function getServerSideProps() {
  const res = await fetch('https://api.example.com/user');
  const data = await res.json();

  return { props: { user: data } };
}
```

### **c) Hooks (React/Next.js)**

```javascript
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(count + 1)}>
      Count: {count}
    </button>
  );
}
```

---

## **6. Key JS Concepts Both Frameworks Use**

1. **Reactive data** (`ref`, `reactive`, `useState`)
2. **Event handlers** (`@click` in Vue, `onClick` in React)
3. **Props & destructuring**
4. **Async operations** (`fetch`, `axios`, `async/await`)
5. **Modules & imports**
6. **ES6 array methods**: `map`, `filter`, `reduce`, `find`, `some`, `every`

```javascript
const arr = [1,2,3,4];
const squared = arr.map(x => x*x);
console.log(squared); // [1,4,9,16]
```

---

✅ **Next Step for You:**

* Practice **Vue Composition API** and **React Functional Components** side by side.
* Focus on **reactivity, props, state, and lifecycle hooks**.
* Write a small project: **Todo app** → this will hit most modern JS features.

