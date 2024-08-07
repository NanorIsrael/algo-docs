const a = new Set([1, 2, 3]);
const b = new Map([
  [1, "one"],
  [2, "two"],
  [4, "four"],
]);
const union = new Set([...a, ...b]);
const intersection = new Set([...a].filter(el => b.has(el)));
const difference = new Set([...a].filter(el => !b.has(el)));

function isSuperset(set, subset) {
	return [...subset].every(el => set.has(el))
}

console.log(union); // Set(4) {1, 2, 3, 4}
console.log(intersection); // Set(4) {1, 2, 3, 4}
console.log(difference); // Set(4) {1, 2, 3, 4}
console.log(isSuperset(union, a)); // Set(4) {1, 2, 3, 4}

const ba = new Set()
ba.add([17, 5])
ba.add([5, 17])
ba.add([5, 7])
console.log(ba)