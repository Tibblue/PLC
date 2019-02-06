grammar gcs18F1Ex2_GIC2;


sa      : 'SA:' nome localizacao negocio socios ags admin funcionarios
        ;

nome    : 'NOME: ' TEXTO ;

localizacao : 'LOCALIZA�AO: ' TEXTO;

negocio : ramo '-' descricao
        ;

ramo    : 'RAMO: agricultura'
        | 'RAMO: industria'
        | 'RAMO: comercio'
        ;
    
descricao : TEXTO;

socios  : socio+
        ;

socio   : 'SOCIO: ' nome ',' cota ';'
        ;

cota    : NUMERO;

ags     : ag*
        ;

ag      : 'Assembleia Geral: ' assunto ': ' decisao
        ;

assunto : TEXTO;

decisao : 'aprovado'
        | 'recusado'
        ;

admin   : 'Administrador: ' TEXTO;

funcionarios : funcionario+
             ;

funcionario : 'FUNCIONARIO: ' nome ',' cargo ',' numero ',' dataNasc ',' dataEntrada ',' telefone ';'
            ;

cargo   : 'Gerente'
        | 'Produ�ao'
        | 'Escritorio'
        | 'Armazem'
        ;

numero  : ('a'..'z')DIGITO+ ;

dataNasc : DATA ;

dataEntrada : DATA ;

telefone : DIGITO DIGITO DIGITO DIGITO DIGITO DIGITO DIGITO DIGITO DIGITO ;




/* Definicao do Analisador LEXICO */
IDENT : LETRA(LETRA|[0-9-_/])* ;

fragment LETRA : [a-zA-Z��������������������������������] ;

TEXTO:    (('\''|'\"') ~('\''|'\"')* ('\''|'\"')); 

DIGITO: [0-9];
NUMERO: ('0'..'9')+ ; // [0-9]+

HORA: [0-9]?[0-9] ':' [0-9][0-9];
DATA: [0-9][0-9] '-' [0-9][0-9] '-' [0-9][0-9];

Separador: ('\r'? '\n' | ' ' | '\t')+  -> skip;



/* NOTAS

Quanto a qualidade achamos que a gramatica nao esta demasiado pesada,
achamos que está equilibrada entre nao ter demasiadas palavras reservadas,
nem ter poucas e dificultar a legivilidade.

*/