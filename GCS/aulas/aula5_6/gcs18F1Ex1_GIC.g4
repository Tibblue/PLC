/*
 * Linguagem: "Acoes de Formacao"
 * Processador: Gramatica Independente de Contexto que permite descrever acoes de formacao
 * PRH 2018.09.24
 */

grammar gcs18F1Ex1_GIC;


acoes     : (acao '.')+
          ;

acao      : cabec  tema  duracao  horario  custo formador alunos
          ;


cabec     : 'FORMACAO:' sigla '-' descricao 
          ;

sigla     : IDENT
          ;

tema      : 'TEMA:' descricao   tipo 
          ;

descricao : TEXTO
          ;

tipo      : 'TIPO:' teor
          | 'TIPO:' prat
          ;

teor      : 'TEORICO'  topicos   bibliografia
          ;

topicos   :    descricaoTopico (';'  descricaoTopico)*
          ;

descricaoTopico : 'TOPICOS:' TEXTO
                ;

bibliografia    :'BIBLIOGRAFIA:' (titulo    obra)+
                ;  

titulo          : 'TITULO:' TEXTO
                ;

obra            : 'OBRA:' TEXTO
                ;

prat            : 'PRATICO'   recursos 
                ;

recursos        : descricaoRecurso (';'  descricaoRecurso)*
                ;


descricaoRecurso : 'RECURSOS:' TEXTO
                 ;

duracao          : 'DURACAO:' NUMERO 'h'
                 ;

horario          : 'HORARIO:' dia '--'  HORA
                 ; 

dia              : '2f'| '3f'| '4f'| '5f'| '6f'| 'sab'
                 ;


custo            : 'CUSTO:' NUMERO
                 ;

alunos           : aluno  (';' aluno)*
                 ;

aluno            : 'ALUNO:' pessoa 
                 ;

formador         : 'FORMADOR:'  pessoa ','  diploma
                 ;
pessoa           : nome ','  morada ',' cartaoC 
                 ;

nome             : TEXTO
                 ;

morada           : TEXTO
                 ;

cartaoC          : TEXTO
                 ;

diploma          : 'tecnico'|'bacharel'|'licenciado'|'mestre'
                 ;




/* Definicao do Analisador LEXICO */
IDENT : LETRA(LETRA|[0-9-_/])* ;

fragment LETRA : [a-zA-ZáéíóúÁÉÍÓÚÃãÕõâêôÂÊÔÀÈÌÒÙàèìòùÇç] ;

TEXTO:    (('\''|'\"') ~('\''|'\"')* ('\''|'\"')); 

NUMERO: ('0'..'9')+ ; // [0-9]+

HORA: [0-9]?[0-9] ':' [0-9][0-9];

Separador: ('\r'? '\n' | ' ' | '\t')+  -> skip;