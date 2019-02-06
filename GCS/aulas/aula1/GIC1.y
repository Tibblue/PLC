
/*
Tema(Descricao) ; Teorico ou pratico
Horario(Dia;hora)
Duracao
Custo
Formador(Diploma{T;B;L;M}) Pessoas
Alunos(Nome;Morada;CC)
*/

%%

Programa 	: Formacoes '.'
		 	;

Formacoes 	: Formacoes ';' Formacao
		  	| Formacao
		  	;

Formacao 	: Sigla ',' Tema ',' Horario ',' Duracao ',' Custo ',' Formador ',' Alunos;

Sigla 	: STR;
Duracao	: STR;
Custo	: STR;

Tema 	: Descricao ':' Tipo;

Descricao	: STR;

Tipo 	: Teorico
	 	| Pratico
	 	;

Teorico : 'TEO' Descricao Titulos
		;

Titulos : Titulos Titulo
		| Titulo
		;

Titulo	: STR;

Pratico : 'PRT' Descricao;

Horario : Slots;

Slots 	: Slots Slot
	  	| Slot
	  	;

Slot 	: Dia '-' Hora
	 	;

Dia		: STR;
Hora 	: STR;

Formador : Pessoa Diploma;

Diploma	: STR;

Aluno 	: Pessoa;

Pessoa 	: Nome Morada Cc;

Nome	: STR;
Morada	: STR;
Cc 		: STR;

%%
