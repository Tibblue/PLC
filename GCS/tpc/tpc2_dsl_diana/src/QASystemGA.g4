grammar QASystemGA;


@header{
        import java.util.*;
        import java.util.stream.Collectors;
}

@members{
         class Triplo{
                      String tipo;
                      ArrayList<String> acoes;
                      ArrayList<String> keywords;
                      String resposta;
                      
            public boolean equals(Triplo t){
                 if (this == null) return false;
                 if (this==t) return true;
                 if (this.getClass() != t.getClass()) return false;
                 
                 return ( (this.tipo).equals(t.tipo) && 
                          (this.acoes).equals(t.acoes) && 
                          (this.keywords).equals(t.keywords));      
            }
            
            public String toString(){
                 StringBuffer sb = new StringBuffer();
                 //sb.append("t = ");
                 sb.append("("+this.tipo+",");
                 sb.append(Arrays.toString(this.acoes.toArray())+",");
                 sb.append(Arrays.toString(this.keywords.toArray())+")");
                 return sb.toString();
            }
           
         }
         
            public String arraytoString(ArrayList<Triplo> arrT){
                StringBuffer sb = new StringBuffer();
                int size = arrT.size();
                for (Triplo t: arrT) {
                    sb.append(t.toString());
                    size--;
                    if (size>0) sb.append (" | ");
                }
                return sb.toString();
            }
            
            public void bcToString(HashMap<String, ArrayList<Triplo>> bc){
            System.out.println("\nBase de Conhecimento:");
                for (String name: bc.keySet()){
                    String key =name.toString();
                    String value = arraytoString(bc.get(name));  
                    System.out.println("key:"+key+ " -> " + value);  
                }
            }


         boolean containsElemList(ArrayList<String> l1, ArrayList<String> l2){
            boolean ret=false;
            int size1 = l1.size();
            int size2 = l2.size();
            
            for(int i=0; i<size1 && !ret; i++)
                for(int j=0; j<size2 && !ret; j++)
                    ret=l2.get(j).toLowerCase().equals(l1.get(i).toLowerCase());
            
            return ret;
         }
}

qas: 'BC:' bcQAS 'QUESTOES:' questoes [$bcQAS.bc]
   ;

questoes [HashMap<String, ArrayList<Triplo>> bc] : (questao [$questoes.bc])+
                                                 { bcToString($bc); }
                                                 ;

/*
vai preenchendo arraylists ao ler cada questão
-> 'tipos', 'acoes' e 'keywords' para chegar à resposta
-> 'palavras' para deteção de acoes e keywords que n estejam a ser detetadas como 'acao'/'keyword' 
-> 'question' para o println da pergunta
*/
questao [HashMap<String, ArrayList<Triplo>> bc]
@init{
    ArrayList<String> tipos = new ArrayList<String>();
    ArrayList<String> acoes = new ArrayList<String>();
    ArrayList<String> keywords = new ArrayList<String>();
    ArrayList<String> palavras = new ArrayList<String>();
    StringBuffer question = new StringBuffer(); 
    question.append("\n");
}
               :( PALAVRA       {palavras.add($PALAVRA.text); question.append($PALAVRA.text).append(" ");} 
                | tipo          {tipos.add($tipo.val); question.append($tipo.val).append(" ");} 
                | acao          {acoes.add($acao.val); question.append($acao.val).append(" ");} 
                | keyword       {keywords.add($keyword.val); question.append($keyword.val).append(" ");} )+ 
                PONTOTERMINAL   {question.append($PONTOTERMINAL.text);}
{                    
        System.out.println("\npalavras: "+Arrays.toString(palavras.toArray())+
                           "\ntipos: "+Arrays.toString(tipos.toArray())+
                           "\nacoes: "+Arrays.toString(acoes.toArray())+
                           "\nkeywords: "+Arrays.toString(keywords.toArray())
                          );
        int tipoSize = tipos.size();
        ArrayList<String> resp = null;
        ArrayList<Triplo> aux = new ArrayList<Triplo>();
                  
        if(tipoSize>0){
            /* entra aqui quando existe um match exato do 'tipo'*/
            for(int i=0;i<tipoSize;i++)
                aux.addAll($bc.get(tipos.get(i)));

            }else{  /* entra aqui quanto, por exemplo, pergunta começa por minúscula*/
                    for(ArrayList<Triplo> l : $bc.values())
                        aux.addAll(l); /*adiciona toda a bc*/
                 }
                 
                 resp = aux.stream()
                        .filter(a -> containsElemList(a.acoes,acoes) || containsElemList(a.acoes,palavras))
                        .filter(a -> containsElemList(a.keywords,keywords) || containsElemList(a.keywords,palavras))
                        .map(a -> a.resposta)
                        .distinct()
                        .collect(Collectors.toCollection(ArrayList::new));
                        
                 System.out.println(question.toString());
                 int w=0;
                 for(String r : resp)
                    System.out.println("R" + w++ + ":" + r);
                 if (resp==null) System.out.println ("Não foi encontrada resposta para a sua pergunta.");
}
;

bcQAS returns [HashMap<String, ArrayList<Triplo>> bc]
@init{$bcQAS.bc = new HashMap<String,ArrayList<Triplo>>();}
              : t1=triplo [$bcQAS.bc] (t2=triplo [$t1.bcOut] {$t1.bcOut = $t2.bcOut;})*
              ;


/* BC é um hashmap de arraylists de Triplos */
triplo [HashMap<String, ArrayList<Triplo>> bcIn] returns [HashMap<String, ArrayList<Triplo>> bcOut]
             : '(' intencao ';' resposta')' 
             {
                $intencao.t.resposta = $resposta.val;
                ArrayList<Triplo> aux = $bcIn.get($intencao.t.tipo);
                if(aux==null) aux = new ArrayList<Triplo>();
                aux.add($intencao.t);
                $bcIn.put($intencao.t.tipo,aux);
                $bcOut = $bcIn;
             }
             ;


intencao returns [Triplo t]
                 : tipo ',' acao ',' keywords
                 {
                    $intencao.t = new Triplo();
                    $intencao.t.tipo = $tipo.val;
                    $intencao.t.acoes = $acao.list;
                    $intencao.t.keywords = $keywords.list;
                 }
                 ;


resposta returns [String val]
                 : TEXTO {$resposta.val = $TEXTO.text;}
                 ;


/* TODO: acrecentar mais tipos */
tipo returns [String val]
             : ( t='Porquê' | t='O quê' | t='Quando' | t='Onde' | t='Como') {$tipo.val = $t.text;}
             ;


/* cria arraylist com as ações (a partir dos triplos da BC) */
acao returns [ArrayList<String> list, String val]
@init{$acao.list = new ArrayList<String>();}
             : 'aceder' {$acao.list.add("aceder"); $acao.list.add("acedo"); $acao.val="aceder";} 
             | 'imprimir' {$acao.list.add("imprimir"); $acao.list.add("imprimo"); $acao.val="imprimir";} 
             | 'inscrever' {$acao.list.add("inscrever"); $acao.list.add("inscrevo"); $acao.val="inscrever";} 
             | 'pagar' {$acao.list.add("pagar"); $acao.list.add("pago"); $acao.list.add("pagam"); $acao.val="pagar";} 
             ;


/* cria arraylist com keywords (a partir dos triplos da BC) */
keywords returns [ArrayList<String> list]
@init{$keywords.list = new ArrayList<String>();}
                 : '[' k1=keyword {$keywords.list.add($k1.val);} ( ',' k2=keyword {$keywords.list.add($k2.val);})* ']' 
                 ;


/* TODO: acrescentar mais keywords */
keyword returns [String val]: 
                ( t='propinas' | t='época' | t='especial' | t='portal' | t='académico' | t='Universidade' | t='Minho') 
                {$keyword.val=$t.text;}
                ;


/* Definição do Analisador Léxico */         
TEXTO:    (('\'') ~('\'')* ('\''));

fragment LETRA : [a-zA-ZáéíóúÁÉÍÓÚÃãÕõâêôÂÊÔÀÈÌÒÙàèìòùÇç] ;

fragment DIGITO: [0-9];

fragment SIMBOLO : [-%$€@&()\[\]{}=><+*;,ºª~^/\'"];

PONTOTERMINAL: [?.!];

PALAVRA: (LETRA | DIGITO | SIMBOLO)+;
/*
fragment PRONOMES: ( ' eu ' | ' me ' | ' mim ' | ' tu ' | ' te ' | ' ti ' | ' ele ' | ' ela '
                                        | ' se ' | ' lhe ' | ' nós ' | ' nos ' | ' vos ' | ' vós ' | ' lhes '
                                        | ' eles ' | ' elas ' )
                                    ;
                     
fragment PROPOSICOES: ( ' ante ' | ' após ' | ' até ' | ' com ' | ' contra '
                                              | ' desde ' | ' em ' | ' entre ' | ' para ' | ' perante ' | ' por ' 
                                              | ' sem ' | ' sob ' | ' sobre ' | ' trás ' ) 
                                          ;

fragment CONJUNCOES : ( ' e ' | ' mas ' | ' ainda ' | ' também ' | ' nem ' | ' contudo '
                                             | ' entretanto ' | ' obstante ' | ' entanto ' | ' porém ' | ' todavia '
                                             | ' já ' | ' ou ' | ' ora ' | ' quer ' | ' assim ' | ' então ' | ' logo '
                                             | ' pois ' | ' conseguinte ' | ' portanto ' | ' porquanto '
                                             | ' porque ' | ' que ' )
                                          ;

fragment DETERMINANTES: ( ' meu ' | ' teu ' | ' seu ' | ' minha ' | ' tua ' | ' sua ' | ' meus '
                                                   | ' teus' | ' seus ' | ' minhas ' | ' tuas ' | ' suas ' | ' nosso '
                                                   | ' vosso ' | ' nossa ' | ' vossa ' | ' nossos ' | ' vossos '
                                                   | ' nossas ' | ' vossas ' | ' este ' | ' esse ' | ' aquele ' | ' esta '
                                                   | ' essa ' | ' aquela ' | ' estes ' | ' esses ' | ' aqueles ' | ' estas '
                                                   | ' essas ' | ' aquelas ' | ' isto ' | ' isso ' | ' aquilo ' | ' todo '
                                                   | ' algum ' | ' nenhum ' | ' outro ' | ' muito ' | ' pouco ' | ' tanto '
                                                   | ' qualquer ' | ' toda ' | ' alguma ' | ' nenhuma ' | ' outra ' | ' muita '
                                                   | ' pouca ' | ' tanta ' | ' todos ' | ' alguns ' | ' nenhuns ' | ' outros '
                                                   | ' muitos ' | ' poucos ' | ' tantos ' | ' quaisquer ' | ' todas '
                                                   | ' algumas ' | ' nenhumas ' | ' outras ' | ' muitas ' | ' poucas ' | ' tantas '
                                                   | ' tudo ' | ' nada ' | ' cada ' | ' ninguém ' | ' alguém ' )
                                                ;

fragment ARTIGOS: ( ' o ' | ' os ' | ' um ' | ' uns ' | ' a ' | ' as ' | ' uma ' | ' umas '
                                     | ' ao ' | ' à ' | ' aos ' | ' às ' | ' em ' | ' num ' | ' numa ' | ' nuns '
                                     | ' numas ' | ' de ' | ' do ' | ' da ' | ' dos ' | ' das ' | ' em '
                                     | ' no ' | ' na ' | ' nos ' | ' nas ' | ' dum ' | ' duma ' | ' duns ' | ' dumas '
                                     | ' pelo ' | ' pela ' | ' pelos ' | ' pelas ' )
                                  ;

fragment NOVALUE : ( ' não ' | PRONOMES | PROPOSICOES | CONJUNCOES | DETERMINANTES | ARTIGOS );
*/
Separador: ( '\r'? '\n' | ' ' | '\t' )+  -> skip; 