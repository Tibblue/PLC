/*
 * Linguagem: "Lista Mista"
 * Processador: Gramatica Independente de Contexto que permite escrever listas mistas de numeros e palavras
 * PRH 2017.09.25
 */

grammar gcs18F2Ex1_GIC;

@header{import java.util.*;}

lista returns[int comprimento, int contaNumeros, float media, int maior, int zona, String erro]
    @init {$lista.erro="";}
    @after{ System.out.println("Comprimento da lista: "+ $lista.comprimento);
            System.out.println("Quantidade de numeros: "+ $lista.contaNumeros);
            System.out.println("Media dos numeros lidos: "+ $lista.media);
            System.out.println("Maior dos numeros lidos: "+ $lista.maior);
            System.out.println("Numero entre start e stop: "+ $lista.zona);
            if($lista.contaNumeros!=$lista.comprimento/2.0) $lista.erro=$lista.erro+"ERRO: Quantidade diferente de palavras e numeros !!!";
            System.out.println($lista.erro);
    }
    : ('LISTA' elems  '.' 
       {$lista.comprimento=$elems.comprimento;
        $lista.contaNumeros=$elems.contaNumeros;
        if($elems.contaNumeros>0) $lista.media=$elems.total/$elems.contaNumeros;
        else $lista.media=0;
        $lista.maior=$elems.maior;
        $lista.zona=$elems.zona;} )+
    ;

elems returns[int comprimento, int contaNumeros, int total, int maior, int zona, boolean zone]
    @init{  $elems.maior=-1;
            $elems.zone=false;
            $elems.zona=0;
    }
    : elem     {$elems.comprimento=1; 
                $elems.contaNumeros=$elem.num; 
                $elems.total=$elem.valor;
                if($elem.num==1 && $elem.valor>$elems.maior) $elems.maior=$elem.valor;
                if($elem.num==0 && $elem.text.equals("start")) $elems.zone=true;
                if($elem.num==0 && $elem.text.equals("stop")) $elems.zone=false;
                if($elems.zone==true) $elems.zona=$elem.valor;}
    (',' elem  {$elems.comprimento++; 
                $elems.contaNumeros+=$elem.num;
                $elems.total+=$elem.valor;
                if($elem.num==1 && $elem.valor>$elems.maior) $elems.maior=$elem.valor;
                if($elem.num==0 && $elem.text.equals("start")) $elems.zone=true;
                if($elem.num==0 && $elem.text.equals("stop")) $elems.zone=false;
                if($elems.zone==true) $elems.zona+=$elem.valor;})*
    ;

elem returns[int num, int valor, String text]
    : NUMERO {$elem.num=1;$elem.valor=$NUMERO.int;$elem.text="";}
    | PAL    {$elem.num=0;$elem.valor=0;$elem.text=$PAL.text;}
    ;

/* Definicao do Analisador LEXICO */

LISTA:  'LISTA';
PAL:    [a-zA-Z][-a-zA-Z_0-9]* ;
NUMERO: '0'..'9'+ ; // [0-9]+

Sep: ('\r'? '\n' | ' ' | '\t')+  -> skip;
