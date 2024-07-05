const a = new Set([1, 2, 3]);
const b = new Map([
  [1, "one"],
  [2, "two"],
  [4, "four"],
]);
const union = new Set([...a, ...b]);
const intersection = new Set([...a].filter(el => b.has(el)));
const difference = new Set([...a].filter(el => !b.has(el)));

console.log(union); // Set(4) {1, 2, 3, 4}
console.log(intersection); // Set(4) {1, 2, 3, 4}
console.log(difference); // Set(4) {1, 2, 3, 4}
