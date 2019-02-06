%{

int size=0;	
int n = 0;
%}



%%

Lista : LISTA Elementos '.'

Elementos : Elementos ',' Elemento {size++;}
		  | Elemento {size++;}
		  ;


Elemento : Numero 
		 | Palavr2a
		 ;

Numero : NUMERO {n++;}
	   ;

Palavra : PALAVRA
		;

%%