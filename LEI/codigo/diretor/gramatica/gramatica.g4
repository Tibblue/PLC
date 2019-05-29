grammar gramatica;

dsl: create_block NEWLINE+ states NEWLINE+ join NEWLINE* EOF;

create_block: (create_bot NEWLINE)+ ;
create_bot: BOT_NAME '=' 'CREATE' BOT_TYPE ('WITH' dataset)? 'FROM' dataset ;

states: 'STATES' STATE+ ;

join: 'JOIN' bots ;

bots: (bot ('+' | NEWLINE))* bot ;
bot : BOT_NAME PRIORIDADE ;

dataset: STRING '.' FILE_TYPE ;

///////////////////////////////////////////////////////////////////////////////

BOT_TYPE: 'bot_csv' | 'bot_lista' | 'bot_wiki'
        | 'bot_QA' | 'bot_exp' | 'bot_FAQ';
FILE_TYPE: 'csv' | 'txt' | 'json' ;
STATE: 'CHATEADO' | 'INFORMATIVO' ;

BOT_NAME: 'b'[0-9]+ ;
PRIORIDADE: '!'[1-5] ;

STRING: [a-zA-Z0-9_\-]+ ;

fragment DIGITO: [0-9] ;

NEWLINE:  '\r'? '\n' ;
WS:       [ \t]+ -> skip ;
