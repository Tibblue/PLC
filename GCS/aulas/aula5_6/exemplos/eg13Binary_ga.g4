/* 
   Linguagem Binaria 
   ano letivo 1314 
   GA: (exemplo classico de Knuth)
*/

grammar eg13Binary_ga;

binary   :  b1=bit[0]
           (b2=bit[$b1.val] {$b1.val = $b2.val;})*
           { System.out.println("Valor decimal do numero binário lido: " + $b1.val); }
         ;
bit      [int valIn]
         returns[int val]   
         : '1' { $bit.val = $bit.valIn*2+1; }
         | '0' { $bit.val = $bit.valIn*2+0; }
         ;

WS       :   [ \t\r\n]  -> skip
         ;
