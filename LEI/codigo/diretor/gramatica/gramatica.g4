grammar gramatica;

dsl: create+ NEWLINE states NEWLINE{2,} join ;

create: BOT_NAME '=' 'CREATE' BOT ('WITH' dataset)? 'FROM' dataset NEWLINE+;

states: 'STATES' STATE+   ;

join: 'JOIN' bot+  ;

bot:  BOT_NAME prioridade_bot '+'
	| BOT_NAME prioridade_bot;

prioridade_bot: '!' PRIORIDADE ;

dataset: STRING '.' FILE_TYPE ;


///////////////////////////////////////////////////////////////////////////////

BOT: 'bot_csv' | 'bot_lista' | 'bot_wiki' | 'bot_QA' | 'bot_exp' | 'bot_FAQ';
FILE_TYPE: 'csv' | 'txt' | 'json' ;
STATE: 'CHATEADO' | 'INFORMATIVO' ;

BOT_NAME: 'b'[0-9] ;

PRIORIDADE: [1-5] ;

STRING: [a-zA-Z0-9_\-]+ ;

fragment DIGITO: [0-9] ;

NEWLINE: '\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace