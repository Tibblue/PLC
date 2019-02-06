/*
 * Linguagem: "Lista Mista"
 * Processador: Contador do Comprimento da lista e quantidade de nums  contidos na lista
 * Uso de gramatica de atributos: apenas atributos sintetizados 
 * PRH 2017.10.02
 */

grammar gcs17F2Ex1abcdef_GA;

lista returns[int comp, int contaN, int soma, float media, String erro, int maximo]
@init
    {
     $lista.erro = "";
     }
@after{ 
        System.out.println("Comprimento da lista: "+ $lista.comp ); 
        System.out.println("Quantidade de Numeros: "+ $lista.contaN );
        System.out.println("Somatorio dos Numeros entre Start e Stop: "+ $lista.soma );
        System.out.println("Média dos números lidos: "+ $lista.media );
        System.out.println("Valor máximo: "+ $lista.maximo);
        System.out.println($lista.erro);
      }
      : 'LISTA' elems  '.'
            { $lista.comp=$elems.comp; 
              $lista.contaN=$elems.contaN; 
              $lista.soma = $elems.total; 
              if($elems.contaN > 0) 
                {$lista.media = $elems.total/$elems.contaN;}
              else $lista.media =0;
         
              if($elems.comp/2.0 != $elems.contaN) 
                 $lista.erro= $lista.erro + "ERRO: quantidades diferentes!";
              if(!$elems.cresc) 
                 $lista.erro = $lista.erro + "\nerro: a lista não é crescente!\n";
                 $lista.maximo = $elems.maximo; 
            }
      ;

elems returns[int comp, int contaN, int total, int maximo, boolean cresc]
      : e1=elem [false,0,true] 
                 {$elems.comp=1; 
                  $elems.contaN=$elem.num; 
                  $elems.total=0; 
                  $elems.maximo = $elem.valor;} 
       (',' e2=elem [$e1.onout,$e1.antOut,$e1.crescOut]
                    {$e1.onout = $e2.onout;
                     $e1.antOut = $e2.antOut;
                     $e1.crescOut = $e2.crescOut;
                     $elems.comp++; 
                     $elems.contaN=$elems.contaN + $elem.num; 
                     if($e2.onout)
                        {$elems.total=$elems.total+$elem.valor;} 
                     if($elem.valor > $elems.maximo) 
                        {$elems.maximo=$elem.valor;}
                    })* 
                    { $elems.cresc = $e1.crescOut; }
      ;

elem [boolean onin, int antIn, boolean crescIn] 
     returns[int num, int valor, boolean onout,int antOut, 
             boolean crescOut]
     : NUMERO {$elem.num=1; 
               $elem.valor=$NUMERO.int; 
               $elem.onout = $elem.onin;
               if($elem.crescIn && $elem.antIn<=$NUMERO.int) {
                  $elem.crescOut = true;
               }else $elem.crescOut = false;
               $elem.antOut = $NUMERO.int;}
     | PAL    {$elem.num=0; 
               $elem.valor=0;
               $elem.antOut = $elem.antIn;
               $elem.crescOut = $elem.crescIn;
               if($PAL.text.equals("start")){$elem.onout=true;}
               else{
                  if($PAL.text.equals("stop")){$elem.onout=false;}
                  else{$elem.onout=$elem.onin;}
               } }
     ;

/* Definicao do Analisador LEXICO */

PAL:    [a-zA-Z][-a-zA-Z_0-9]* ;

NUMERO: '0'..'9'+ ; 

Sep: ('\r'? '\n' | ' ' | '\t')+  -> skip;