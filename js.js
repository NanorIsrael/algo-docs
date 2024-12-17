function resolveAfter2Seconds() {
	console.log("starting slow promise");
	return new Promise((resolve) => {
	  setTimeout(() => {
		resolve("slow");
		console.log("slow promise is done");
	  }, 2000);
	});
  }
  
  function resolveAfter1Second() {
	console.log("starting fast promise");
	return new Promise((resolve) => {
	  setTimeout(() => {
		resolve("fast");
		console.log("fast promise is done");
	  }, 1000);
	});
  }
  
  async function sequentialStart() {
	console.log("== sequentialStart starts ==");
  
	// 1. Start a timer, log after it's done
	const slow = resolveAfter2Seconds();
	console.log(await slow);
  
	// 2. Start the next timer after waiting for the previous one
	const fast = resolveAfter1Second();
	console.log(await fast);
  
	console.log("== sequentialStart done ==");
  }
  
  async function sequentialWait() {
	console.log("== sequentialWait starts ==");
  
	// 1. Start two timers without waiting for each other
	const slow = resolveAfter2Seconds();
	const fast = resolveAfter1Second();
  
	// 2. Wait for the slow timer to complete, and then log the result
	console.log(await slow);
	// 3. Wait for the fast timer to complete, and then log the result
	console.log(await fast);
  
	console.log("== sequentialWait done ==");
  }
  
  async function concurrent1() {
	console.log("== concurrent1 starts ==");
  
	// 1. Start two timers concurrently and wait for both to complete
	const results = await Promise.all([
	  resolveAfter2Seconds(),
	  resolveAfter1Second(),
	]);
	// 2. Log the results together
	console.log(results[0]);
	console.log(results[1]);
  
	console.log("== concurrent1 done ==");
  }
  
  async function concurrent2() {
	console.log("== concurrent2 starts ==");
  
	// 1. Start two timers concurrently, log immediately after each one is done
	await Promise.all([
	  (async () => console.log(await resolveAfter2Seconds()))(),
	  (async () => console.log(await resolveAfter1Second()))(),
	]);
	console.log("== concurrent2 done ==");
  }
  
//   sequentialStart(); // after 2 seconds, logs "slow", then after 1 more second, "fast"
  
  // wait above to finish
//   setTimeout(sequentialWait, 4000); // after 2 seconds, logs "slow" and then "fast"
  
//   // wait again
//   setTimeout(concurrent1, 7000); // same as sequentialWait
  
//   // wait again
//   setTimeout(concurrent2, 10000); // after 1 second, logs "fast", then after 1 more second, "slow"
  
function  bubbleSort(myarr=[1,8, 4, 5,2,6,3,7]){
	isSorted = true
	// let idx = 0
	while (isSorted) {
		isSorted = false
		let temp = 0
		for (let idx=0; idx < myarr.length - 1; idx++) {
			if (myarr[idx] > myarr[idx + 1]) {
				temp = myarr[idx + 1]
				myarr[idx + 1] = myarr[idx]
				myarr[idx] = temp
				isSorted = true
			}
		}
	}
	return myarr
}

const myarr=[1,8, 4, 5,2,6,3,7]
// console.log(myarr.with(0,21))

const questions = [{id: 1, text: "Free"}, {id: 2, text: "who Free bag are you "}, {id: 3, text: "free bag"}]


console.log(questions.map((obj) => obj.text.toLowerCase().search(/^(free bag)/)))
console.log(questions.map((obj) => obj.text.match(/^(free bag)/i)))
console.log(questions.map((obj) => obj.text.toLowerCase().includes('free')))


function is_match(s, p) {
	if (!p){
		return false
	}
		
	const first_match = Boolean(s) && (s[0] == p[0] || p[0] == '.')
	if (p.length  >= 2 && p[1] === '*') {
		const case1 = is_match(s, p[p.slice(2)])
		const case2 = first_match && is_match(s[s.slice(1)], p)
		return case1 || case2
	}
		
	return first_match && is_match(s[s.slice(1)], p[p.slice(1)])
}
// console.log(is_match("aa", "a"))     
// console.log(is_match("aa", "a*"))    
// console.log(is_match("ab", ".*"))    
// console.log(is_match("aab", "c*a*b"))


const s1 = 'namelesss'
const s2 = 'salesmen'

function sol(s1, s2) {
	if (s1.length != s2.length) {
		return false;
	}
	const sortedS1 = s1.replace('\s+\g', '')
	const sortedS2 = s2.replace('\s+\g', '')

	const charCount = {}
	for (let char of sortedS1) {
		charCount[char] = (charCount[char] || 0) + 1
	}

	for (let char of sortedS2) {
		if (!charCount[char]) return false
		charCount[char] --
	}
	return true

}
console.log(sol(s1, s2))
