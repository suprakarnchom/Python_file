// Example JSON string
const jsonString = '{"name": "John", "age": 30, "city": "New York"}';

// Parse the JSON string
const jsonData = JSON.parse(jsonString);

console.log(jsonData);  // Output: { name: "John", age: 30, city: "New York" }

// Now you can access the data using JavaScript object notation
console.log(jsonData.name);  // Output: John

