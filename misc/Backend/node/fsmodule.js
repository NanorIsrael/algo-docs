const readline = require('readline')
const rl = readline.createInterface(process.stdin, process.stdout)
const fs =  require('fs')


const person = {
	name: '',
	sayings: []
} 
rl.question("what is your name:\n", (answer) => {
	// console.log(answer)
	person.name = answer
	const writeStream = fs.createWriteStream(`${answer}.md`)
	writeStream.write(`${answer}\n ============================ \n\n`)
	rl.setPrompt(`What would ${answer} say?\n`)
	rl.prompt()

	rl.on('line', (saying) => {
		if (saying.toLowerCase() === 'exit') {
			writeStream.close()
			rl.close()
		} else {
			person.sayings.push(saying)
			writeStream.write(`* ${saying.trim()}\n`, () => null)	
			rl.setPrompt(`What else would ${person.name} say? ('exit' to leave)\n`)
			rl.prompt()
		}
	})
})