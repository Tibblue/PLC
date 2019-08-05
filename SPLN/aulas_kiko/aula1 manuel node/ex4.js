#!/usr/bin/env node

const readline = require('readline');
const removeAccent = require('diacritics').remove;

/*
const rl = readline.createInterface({
	input: process.stdin,
	//output: process.stdout
}); */

var answer = 'Bom dia! Tudo bem? Sim. Há, mas são verdes.';

// Colocar todas as letras em minúsculas.
var processed = answer.toLowerCase();

// Separar palavras e pontuação por espaços.
const palavra = '[a-z0-9A-ÿ]+'
const pontuacao = '[\.:,;/&]+'
const regexToMatch = new RegExp('\s*(' + palavra + '|' + pontuacao + ')\s*', 'g');

processed = processed.replace(regexToMatch, (substring) => {
	return substring + ' ';
});

// Remover acentuação dos caracteres
processed = removeAccent(processed);

processed = processed.replace(/[\s]+/g, ' ');

//var acentos = /[A-ÿ]/g;
/*
processed = processed.replace(acentos, (substring) => {
	return removeAccent(substring);	
});*/

console.log(processed);
