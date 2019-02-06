%{
#include <stdio.h>
#include <math.h>
extern int yylex();
extern char *yytext;
extern int yylineno;
void yyerror(char *);

int size=0, nums=0, media=0;
%}

%token NUMERO PALAVRA
%union{
    int num;
    char* palavra;
}
%type <num> NUMERO
%type <palavra> PALAVRA 


%%

Lista   : LISTA Elementos '.'
        ;

Elementos : Elementos ',' Elemento  
        | Elemento                  
        ;

Elemento : NUMERO   {size++;nums++;}
        | PALAVRA   {size++;}
        ;

%%
