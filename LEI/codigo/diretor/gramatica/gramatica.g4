grammar gramatica;

dsl: create* | states | join ;

create: bot_name '=' 'CREATE' BOT ('WITH' dataset)? 'FROM' dataset ;

states: estado* ;

join: 'JOIN' (bot_name prioridade_bot '+')* | bot_name prioridade_bot ;

////////////////////////////////////////

bot_name: 'b' NUMERO ;

prioridade_bot: '!' PRIORIDADE ;

dataset: STRING '.' FILE_TYPE ;

estado: STRING ;

///////////////////////////////////////////////////////////////////////////////

PRIORIDADE: [1-5] ;

NUMERO: [0-9]+ ;

STRING: [a-zA-Z0-9_\-] ;

BOT: 'bot_csv' | 'bot_lista' | 'bot_wiki' | 'bot_QA' | 'bot_exp' | 'bot_FAQ';

FILE_TYPE: 'csv' | 'txt' | 'json' ;