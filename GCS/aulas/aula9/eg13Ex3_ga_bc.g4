/* 
   Linguagem Faturas 
   ano letivo 1314 
   GA: parte b e c)
*/

grammar eg13Ex3_ga_bc;

@header{
        import java.util.*;
}

@members{
          class Produto{
           String desc;
           Double precU;
           Double qtS;
           
           public String toString(){
                 StringBuffer sb = new StringBuffer();
                 sb.append(this.desc+"; ");
                 sb.append(this.precU+"; ");
                 sb.append(this.qtS+". ");
                 return sb.toString();
                 }
           }         
}

faturas : stock fats[$stock.armazem]
        ;
        
fats [HashMap<String, Produto> armazem]
        :  f1=fatura[$fats.armazem] {$fats.armazem = $f1.armazem;}
          (f2=fatura[$fats.armazem] {$fats.armazem = $f2.armazem;})*
           { System.out.println("Quantidades em Armazem no fim:"); 
           System.out.println($f1.armazem.toString()); } 
        ;
stock    returns[HashMap<String, Produto> armazem]
@init    { $stock.armazem = new HashMap<String, Produto>(); }
         : 'STOCK' 
            p1=produto[$stock.armazem] { $stock.armazem=$p1.armazemOut; }
           (p2=produto[$stock.armazem] { $stock.armazem=$p2.armazemOut; })*
         { System.out.println("Quantidades em Armazem no inicio:"); System.out.println($stock.armazem.toString()); } 
         ;
produto  [HashMap<String, Produto> armazemIn]
         returns[HashMap<String, Produto> armazemOut]
         :  refProd ':' descProd ';' valUnit ';' quantS
         {  Produto p = new Produto(); 
            p.desc=$descProd.text; p.precU=Double.parseDouble($valUnit.text); p.qtS=Double.parseDouble($quantS.text);
            $produto.armazemIn.put($refProd.text, p); 
            $produto.armazemOut=$produto.armazemIn;
         }
         ;

fatura   [HashMap<String, Produto> armazemIn]
         returns[HashMap<String, Produto> armazem]
         : 'FATURA' cabec 'VENDAS' corpo[$fatura.armazemIn]
         {  
            System.out.println("TOTAL da Fatura: "+ $corpo.totF);
            $fatura.armazem = $corpo.armazem; 
         }
         ;
cabec    : numFat idForn 'CLIENTE' idClie 
         { System.out.println("FATURA num: " + $numFat.text);}
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
corpo    [HashMap<String, Produto> armazemIn]
         returns[HashMap<String, Produto> armazem, Double totF]
@init    { System.out.println("Totais Parciais:"); }
         :  l1=linha[$corpo.armazemIn]  '.' { $corpo.totF = $l1.totL;  $corpo.armazem = $l1.armazem; }
           (l2=linha[$corpo.armazem] '.'    { $corpo.totF += $l2.totL; $corpo.armazem = $l2.armazem; })*
         ;
linha    [HashMap<String, Produto> armazemIn]
         returns[HashMap<String, Produto> armazem, Double totL]
         : refProd '|'  quant
         { Produto p;
                if ($linha.armazemIn.containsKey($refProd.text)) { 
                   p = $linha.armazemIn.get($refProd.text); 
                   System.out.println($refProd.text +"-> "+ (p.precU *(Double.parseDouble($quant.text))));
                   $linha.totL = (p.precU * (Double.parseDouble($quant.text))); 
                   p.qtS -= (Double.parseDouble($quant.text)); 
                   $linha.armazemIn.put($refProd.text,p);  
                 }
           else  { System.out.println("ERRO: A Referencia " + $refProd.text + " nao existe em Stock"); 
                   $linha.totL = 0.0; 
                 } 
           $linha.armazem = $linha.armazemIn;
         }
         ;
refProd  : ID  
         ;
valUnit  : NUM 
         ;
quant    : NUM 
         ;
descProd : STR 
         ;
quantS   : NUM 
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
