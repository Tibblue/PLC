grammar gestaoEventos;

evento : nomeEvento dataEvento hora local descricao custoAssociado listaParticipantes ;

nomeEvento: 'Evento:' nome ;

dataEvento: 'Data:' data ;

hora: 'Hora:' horas;

local: 'Local: ' localidade ;

descricao: 'Descricao:' desc ;

custoAssociado: 'Custo:' custo '€' ;

listaParticipantes: 'Participantes:' participantes;

participantes: (participante ',')*  participante '.';

participante : nome ;

nome  : STRING {$n = $STRING.text};

data : NUMERO '-' NUMERO '-' NUMERO ;

localidade : STRING{$loc=$STRING.text};

desc : STRING {$des = $STRING.text};

horas : NUMERO ':' NUMERO ;

custo : NUMERO ;

/* ----- LEXER ----- */
NUMERO: DIGITO+;

fragment DIGITO: [0-9];

STRING:  '"' ~["]* '"';


SEPARADOR: ('\r'? '\n' | ' ' | '\t') -> skip;