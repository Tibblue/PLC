/* 
   Linguagem Faturas 
   ano letivo 1314 
   GA: parte a)
*/

grammar eg13Ex3_ga_a;

faturas : fatura +
         ;
fatura   : 'FATURA' cabec 'VENDAS' corpo
         { System.out.println("Total da Fatura <" + $cabec.ref + ">: " + $corpo.totF); }
         ;
cabec    returns[String ref]
         : numFat idForn 'CLIENTE' idClie 
         { $cabec.ref = $numFat.text; }
         ;
numFat   : ID
         ;
idForn   : nome morada 'NIF:' nif  'NIB:' nib
         ;
idClie   : nome morada 'NIF:' nif
         ;
nome     : STR
         ;
nif      : STR
         ;
morada   : STR
         ;
nib      : STR
         ;
corpo    returns[Double totF] 
@init    { System.out.println("Totais Parciais:"); }
         :  linha '.' { $corpo.totF  = $linha.totL; }
           (linha '.' { $corpo.totF += $linha.totL; })*
         ;
linha     returns[Double totL]
         : refProd '|' pr=valUnit '|' qt=quant
         { System.out.println($refProd.text +"-> "+ (Double.parseDouble($pr.text) * Double.parseDouble($qt.text))); 
           $linha.totL = (Double.parseDouble($pr.text) * Double.parseDouble($qt.text)); 
         }
         ;
refProd  : ID
         ;
valUnit  : NUM 
         ;
quant    : NUM 
         ;

         
/*--------------- Lexer ---------------------------------------*/

ID  :	('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_'|'-')*
    ;

NUM :	'0'..'9'+('.'('0'..'9')+)?
    ;

WS  :   [ \t\r\n]  -> skip
    ;
    
STR
    :  '"' ( ESC_SEQ | ~('"') )* '"'
    ;

fragment
ESC_SEQ
    :   '\\' ('b'|'t'|'n'|'f'|'r'|'\"'|'\''|'\\')
    |   UNICODE_ESC
    |   OCTAL_ESC
    ;
 
fragment
OCTAL_ESC
    :   '\\' ('0'..'3') ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7')
    ;

fragment
UNICODE_ESC
    :   '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
    ;
fragment
HEX_DIGIT : ('0'..'9'|'a'..'f'|'A'..'F') 
    ;
