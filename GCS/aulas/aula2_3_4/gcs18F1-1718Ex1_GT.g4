/*
 * Linguagem: "Lista Mista"
 * Processador: Gramatica Independente de Contexto que permite escrever listas mistas de numeros e palavras
 * PRH 2017.09.25
 */

grammar gcs18F1-1718Ex1_GT;

@members{int tam=0; int soma=0;}

lista : ('LISTA' elems  '.' 
        {System.out.println("Tamanho: " + tam + " ; Somatório " + soma); tam=soma=0;} )+
      ;

elems : elem  /*{tam=1;}*/ 
        (',' elem /*{tam++;}*/)*   
      ;

elem : NUMERO {tam++; soma+=$NUMERO.int;}
     | PAL   {tam++;}
     ;


/* Definicao do Analisador LEXICO */

PAL:    [a-zA-Z][-a-zA-Z_0-9]* ;

NUMERO: '0'..'9'+ ; // [0-9]+

Sep: ('\r'? '\n' | ' ' | '\t')+  -> skip;
