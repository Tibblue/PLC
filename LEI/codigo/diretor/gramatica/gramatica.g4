grammar gramatica;

dsl: create_block NEWLINE+ states NEWLINE* EOF;

create_block: (create_bot NEWLINE)+ ;
create_bot: PRIORIDADE 'CREATE' BOT_TYPE ('WITH' dataset)? 'FROM' dataset ;

states: 'STATES' STATE+ ;

dataset: STRING '.' FILE_TYPE ;

///////////////////////////////////////////////////////////////////////////////

BOT_TYPE: 'bot_csv' | 'bot_lista' | 'bot_wiki' | 'bot_QA'
        | 'bot_exp' | 'bot_FAQ' | 'bot_tradutor';
FILE_TYPE: 'csv' | 'txt' | 'json' ;
STATE: 'CHATEADO' | 'INFORMATIVO' ;

PRIORIDADE: '!'[0-5] ;

STRING: [a-zA-Z0-9_\-]+ ;

NEWLINE:  '\r'? '\n' ;
WS:       [ \t]+ -> skip ;
