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
	fs.writeFileSync(`${answer}.md`, `${answer}\n ============================ \n\n`)
	rl.setPrompt(`What would ${answer} say?\n`)
	rl.prompt()

	rl.on('line', (saying) => {
		person.sayings.push(saying)
		fs.appendFile(`${person.name}.md`, `* ${saying.trim()}\n`, () => null)

		if (saying.toLowerCase() === 'exit') {
			rl.close()
		} else {
			rl.setPrompt(`What else would ${person.name} say? ('exit' to leave)\n`)
			rl.prompt()
		}
	})
})