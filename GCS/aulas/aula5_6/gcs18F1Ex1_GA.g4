grammar gcs18F1Ex1_GA;

acoes
    @init{
        int numAcoes=0;
    }
    @after{
        System.out.println("Numero de acoes: " + numAcoes);
    }
        : (acao '.' {numAcoes++;})+ 
        ;

acao    : cabec tema duracao horario custo formador alunos
            {
                System.out.println("Numero de alunos na acao " + $cabec.siglaText + " : " + $alunos.numAlunos);
                System.out.println("Numero de semanas na acao " + $cabec.siglaText + " : " + $duracao.val/(double)$horario.horas);
                if($tema.ePratica && $alunos.numAlunos>5){
                    System.out.println("Erro em " + $cabec.siglaText + ": Uma turma pratica não pode ter mais do que 5 alunos!!!");
                }
                if(!$tema.ePratica && !$formador.eLicencOuMestre){
                    System.out.println("Erro em " + $cabec.siglaText + ": O formador de aulas teoricas tem de ser licenciado ou mestre!!!");
                }
            }
        ;


cabec returns[String siglaText]
        : 'FORMACAO:' sigla '-' descricao 
            {$cabec.siglaText=$sigla.value;}
        ;

sigla returns[String value]
        : IDENT {$sigla.value=$IDENT.text;} ;

tema returns[boolean ePratica]
        : 'TEMA:' descricao tipo {$tema.ePratica=$tipo.ePratica;}
        ;

descricao : TEXTO ;

tipo returns[boolean ePratica]
        : 'TIPO:' teorica {$tipo.ePratica = false;}
        | 'TIPO:' pratica {$tipo.ePratica = true;}
        ;

teorica : 'TEORICO' topicos bibliografia
        ;

topicos :    descricaoTopico (';' descricaoTopico)*
        ;

descricaoTopico : 'TOPICOS:' TEXTO ;

bibliografia :'BIBLIOGRAFIA:' (titulo obra)+
             ;

titulo  : 'TITULO:' TEXTO ;

obra    : 'OBRA:' TEXTO ;

pratica : 'PRATICO' recursos 
        ;

recursos : descricaoRecurso (';' descricaoRecurso)*
         ;


descricaoRecurso : 'RECURSOS:' TEXTO ;

duracao returns[int val]
		: 'DURACAO:' NUMERO 'h' {$duracao.val = $NUMERO.int;}
		;

horario returns[double horas]
        : 'HORARIO:' dia ',' h1=hora '--' h2=hora {$horario.horas=$h2.val-$h1.val;}
        ; 

dia     : '2f'| '3f'| '4f'| '5f'| '6f'| 'sab'
        ;

custo   : 'CUSTO:' NUMERO ;

alunos returns[int numAlunos]
        : aluno      {$alunos.numAlunos=1;}
          (';' aluno {$alunos.numAlunos++;} )* 
        ;

aluno   : 'ALUNO:' pessoa 
        ;

formador returns[boolean eLicencOuMestre]
            : 'FORMADOR:' pessoa ',' diploma
                {
                    if($diploma.text.equals("licenciado") || $diploma.text.equals("mestre"))
                        $formador.eLicencOuMestre=true;
                    else 
                        $formador.eLicencOuMestre=false;
                }
            ;

pessoa  : nome ',' morada ',' cartaoC 
        ;

nome    : TEXTO ;

morada  : TEXTO ;

cartaoC : TEXTO ;

diploma : 'tecnico'|'bacharel'|'licenciado'|'mestre' ;

hora returns[double val]
		: h=NUMERO ':' m=NUMERO {$hora.val = $h.int + $m.int/60.0;}
		;

/* Definicao do Analisador LEXICO */
IDENT : LETRA(LETRA|[0-9-_/])* ;

fragment LETRA : [a-zA-Z��������������������������������] ;

TEXTO : (('\''|'\"') ~('\''|'\"')* ('\''|'\"')); 

NUMERO : ('0'..'9')+ ; // [0-9]+

/*HORA : [0-9]?[0-9] ':' [0-9][0-9];*/

Separador : ('\r'? '\n' | ' ' | '\t')+  -> skip;