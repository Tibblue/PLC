grammar grupo3GIC;

//Area de conhecimento: Portugal
qas     : 'Base Conhecimento:' baseQAS 'Questoes:' questoes
        ;

baseQAS : triplo+ ;

triplo: '(' intencao ';' resposta ';' confianca ')';
         

intencao: TIPO ';' acao ';' keywords ;

acao: ( ( 'ser' )  | ('ganhar') | 'tem' | 'haver' );

keywords: KEYWORD (',' KEYWORD)* ;

questoes : questao+ ;

questao : 'Q:' (TIPO | ACAO | KEYWORD | PALAVRA)+ SIMBOLOTERMINAL ;

resposta: TEXTO ;

confianca: NUMERO;

/* ----- LEXER ----- */
TIPO    : 'Porque' | 'Quem' | 'Quando' | 'Onde' | 'Como' | 'Qual';
ACAO    : 'fez' | 'foi' | 'liderou' | 'ganhou' | 'inclui' | 'é' | 'foram';
KEYWORD : 'rei' | 'batalha' | 'primeiro' | 'descoberto' | 'Brasil' | 'terramoto' |
        'famoso' | 'republica' | 'segunda' | 'maior' | 'primeira' | 'cidade' | 'serra' |
        'mais' | 'alta' | 'regiao' | 'distrito' | 'Beja' | 'presidente' | 'liga' |
        'futebol' | '2014/2015' | 'desapareceu' | 'segundo';

TEXTO:  '"' ~["]* '"';

NUMERO: DIGITO+;
PALAVRA: (LETRA)+;
fragment DIGITO: [0-9];
fragment LETRA: [a-zA-Záé];

SIMBOLOTERMINAL: [?.!];

SEPARADOR: ('\r'? '\n' | ' ' | '\t') -> skip;
