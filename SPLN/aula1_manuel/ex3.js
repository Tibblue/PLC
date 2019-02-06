#!/usr/bin/env node

const readline = require('readline');
const fs = require('fs');

const filename = process.argv[2];
const stream = fs.createReadStream(filename); 
const rl = readline.createInterface({
	input: stream, // O stdin passará a ser o ficheiro!
	//output: process.stdout
});

var fileLines = [];

rl.on('line', (input) => {
	fileLines.push(input);
}).on('close', () => {
	fileLines.reverse().forEach(line => console.log(line));
});
