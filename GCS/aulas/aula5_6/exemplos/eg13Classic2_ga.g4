/*
   Linguagem de Strings de comprimento controlado
   ano letivo 13/14
   GA: (2. exemplo classico)
*/

grammar eg13Classic2_ga;

string   :  NUM list[$NUM.int]
         { if ($list.len==0) { System.out.println("String lida de comprimento correto: " + $list.val); }
           else { System.out.println("String lida (" + $list.val + ") nao tem o comprimento esperado (" + $NUM.int + ") !"); }
         } 
         ;
list     [int lenIn]
         returns[int len, String val]
         : '[' (chars[$lenIn])? ']' 
         { if ($chars.text!=null) { $list.len = $chars.len; $list.val = $chars.val; }
           else { $list.len=$list.lenIn; $list.val=""; }
         }
         ;
chars    [int lenIn]
         returns[int len, String val]
         :  c1=CHAR { $chars.len = $chars.lenIn-1; $chars.val = $c1.text; }
           (c2=CHAR { $chars.len--; $chars.val += $c2.text; })*
         ;
         
/*--------------- Lexer ---------------------------------------*/

CHAR     :	('a'..'z'|'A'..'Z') 
         ;

NUM      :	'0'..'9'+
         ;

WS       :   [ \t\r\n]  -> skip
         ;
