%{
    #include "y.tab.h"
%}

%%
[ \t\n]     ;
[,.]        return *yytext;

LISTA       { yylval.palavra=yytext;
                    return LISTA; }
[a-z]+      { yylval.palavra=yytext;
                    return PALAVRA; }
[0-9]       { yylval.num=atoi(yytext);
                    return NUMERO; }

.           return ERRO;
