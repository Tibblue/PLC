#!/usr/bin/env node

const readline = require('readline');
const Promise = require('bluebird'); // Faz override às promises normais (mais clean)
const util = require('util');

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

//const question = util.promisify(rl.question);
/*
question('String: ')
	.then(input => console.log(input))
	.catch(erro => console.log('Erro: ' + erro)); */


rl.question('String: ', input => {
	console.log(input.toUpperCase());

	rl.close();
});
