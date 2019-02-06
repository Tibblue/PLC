grammar gestaoEventos;

evento : nomeEvento dataEvento hora local descricao custoAssociado listaParticipantes ;

nomeEvento: 'Evento:' nome
          ;

dataEvento: 'Data:' data
          ;

hora: 'Hora:' horas;

local: 'Local: ' localidade ;

descricao: 'Descrição:' desc ;

custoAssociado: 'Custo:' custo '€' ;

listaParticipantes: 'Participantes:' participantes;

participantes: (participante ',')*  participante '.';

participante : nome ;

nome : STRING;

data : NUMERO '-' NUMERO '-' NUMERO;

localidade: STRING;

desc: STRING;

horas: NUMERO ':' NUMERO;

custo: NUMERO;
            
/* ----- LEXER ----- */


NUMERO: DIGITO+;

fragment DIGITO: [0-9];

STRING:  '"' ~["]* '"';

SEPARADOR: ('\r'? '\n' | ' ' | '\t') -> skip;