grammar grupo3GA;

@header {
    import java.util.List;
    import java.util.*;
    import java.lang.String;
    import java.util.HashMap;
}
@members {
    class Triplo{
        String tipoQ;
        List<String> acoes;
        List<String> keywords;
        String resposta;
        int confianca;
    
        public String toString(){
            StringBuffer sb = new StringBuffer();
            sb.append(this.tipoQ+"; ");
            for( String a : acoes){
                sb.append(a+"; ");
            }
            for( String k : keywords){
                sb.append(k+"; ");
            }
            sb.append(this.resposta+"; ");
            sb.append(this.confianca+"; ");
            return sb.toString();
        }
    }
}

//Area de conhecimento: Portugal
qas     : 'Base Conhecimento:' baseQAS 'Questoes:' questoes[$baseQAS.triplos]
        ;

baseQAS returns[List<Triplo> triplos]
    @init{
         $baseQAS.triplos = new ArrayList<Triplo>();
    }
        : (triplo{$baseQAS.triplos.add($triplo.t);})+
        ;

triplo returns [Triplo t]
    @init{
        $triplo.t = new Triplo();
    } 
        : '(' intencao
          ';' resposta
          ';' confianca 
          ')'
            {
                $triplo.t.tipoQ = $intencao.tipoQ;
                $triplo.t.acoes = $intencao.acoes;
                $triplo.t.keywords = $intencao.keywordsOut;
                $triplo.t.resposta=$resposta.text;
                $triplo.t.confianca=$confianca.val;
            }
        ;
         

intencao returns[String tipoQ,List<String> acoes, List<String> keywordsOut]
        : t=TIPO ';' acao ';' keywords 
          {
           $intencao.tipoQ=$t.text;
           $intencao.acoes=$acao.listaAcoes;
           $intencao.keywordsOut=$keywords.keywordsOut;
          }
        ;

acao returns [ArrayList<String> listaAcoes]
@init{$acao.listaAcoes = new ArrayList<String>();}
         : ( 
           ( 'ser' ) {$acao.listaAcoes.add("�"); $acao.listaAcoes.add("foi");$acao.listaAcoes.add("foram");}
           | ('ganhar') {$acao.listaAcoes.add("ganhou");$acao.listaAcoes.add("ganharam");}
           | 'tem' {$acao.listaAcoes.add("tem"); $acao.listaAcoes.add("teve"); $acao.listaAcoes.add("tinha");}
           | 'haver' {$acao.listaAcoes.add("h�"); $acao.listaAcoes.add("havia"); $acao.listaAcoes.add("houve");}
           )
         ;

keywords returns[List<String> keywordsOut]
    @init{
        $keywords.keywordsOut = new ArrayList<String>();
    }
        : k1=KEYWORD {$keywords.keywordsOut.add($k1.text);}
          (',' k2=KEYWORD {$keywords.keywordsOut.add($k2.text);})*
        ;

questoes [List<Triplo> triplos]
    @init{
         int keysQ,questaoCheck=0,verboCheck=0,valor,flag=0,ratioAux;
         double ratio,conf,confMax;
         }
    : (questao
       {
        Set<String> listaR = new HashSet<>();

        for(String p : $questao.pergunta){
            System.out.print(p);
            System.out.print(" ");
        }
        System.out.println();
        confMax=0;
        for(Triplo t : triplos){                   
             keysQ = 0;
             
             // verifica se a tipo de quest�o � igual � do triplo
             if($questao.listaQ.contains(t.tipoQ))
                questaoCheck=1;
             
             // verifica se o tipo de verbo � igual � do triplo
             for(String a : t.acoes)
                 if($questao.listaV.contains(a)) verboCheck=1;                      
            
             // caso o tipoQ e verbo coincida vai ver o n�mero de keywords
             if(questaoCheck==1 && verboCheck==1 ){
                 
                // conta o numero de keywords que a questao tem relativas ao triplo 
                if(t.keywords.size() > $questao.listaK.size()){                                         
                    for(String k : $questao.listaK)
                         if(t.keywords.contains(k)) keysQ++;
                    ratioAux = t.keywords.size();
                 }
                else{
                    for(String k : t.keywords)
                         if($questao.listaK.contains(k)) keysQ++;
                    ratioAux = $questao.listaK.size();
                }
                
                // caso tenha no minimo uma key em comuns talvez possa ser a resposta
                if(keysQ>0){
                    // flag representa que encontrou alguma resposta
                    flag = 1;
                    
                    // calcula o ratio
                    ratio = keysQ*1.0/ratioAux*1.0;
                    conf = t.confianca * ratio;
                    
                    // adiciona outra resposta se a conf for a mesma
                    if(conf == confMax){                        
                         listaR.add(t.resposta);
                    }
                    
                    // se o valor da conf for maior que o definido guarda a resposta do triplo
                    else if(conf > confMax){
                            listaR.clear();
                            confMax=conf;
                            listaR.add(t.resposta);
                    }
                }

             }
             
        }
        valor = (int)confMax;
        
        if(flag==1) {
                for(String r : listaR){
                    System.out.println("Resposta: " + r + " Confian�a: " + valor);
                    }
                System.out.println();
        }
       }
      )+
        ;

questao returns [List<String> listaQ,List<String> listaV, List<String> listaK, List<String> pergunta]
    @init{
        $questao.listaQ = new ArrayList<String>();
        $questao.listaV = new ArrayList<String>();
        $questao.listaK = new ArrayList<String>();
        $questao.pergunta = new ArrayList<String>();
         }
    : 'Q:' (TIPO  {
                  $questao.listaQ.add($TIPO.text);
                  $questao.pergunta.add($TIPO.text);
                      
                  } 
           | ACAO {
                  $questao.listaV.add($ACAO.text);
                  $questao.pergunta.add($ACAO.text);
                      
                  }
           | KEYWORD{
                  $questao.listaK.add($KEYWORD.text);
                  $questao.pergunta.add($KEYWORD.text);
                        
                  }
           | PALAVRA{
                   $questao.pergunta.add($PALAVRA.text);
                  }
           )+ SIMBOLOTERMINAL {
                   $questao.pergunta.add($SIMBOLOTERMINAL.text);
                  }      
    ;

resposta: TEXTO ;

confianca returns[int val]
    : NUMERO {$confianca.val=$NUMERO.int;}
    ;

/* ----- LEXER ----- */
TIPO    : 'Porque' | 'Quem' | 'Quando' | 'Onde' | 'Como' | 'Qual';
ACAO    : 'fez' | 'foi' | 'liderou' | 'ganhou' | 'inclui' | '�' | 'foram';
KEYWORD : 'rei' | 'batalha' | 'primeiro' | 'descoberto' | 'Brasil' | 'terramoto' |
        'famoso' | 'republica' | 'segunda' | 'maior' | 'primeira' | 'cidade' | 'serra' |
        'mais' | 'alta' | 'regiao' | 'distrito' | 'Beja' | 'presidente' | 'liga' |
        'futebol' | '2014/2015' | 'desapareceu' | 'segundo';
// TIPO    : 'PorquÃƒÂª' | 'Quem' | 'Quando' | 'Onde' | 'Como' | 'Qual' | 'Em que';
// ACAO    : 'fez' | 'foi' | 'liderou' | 'desapareceu' | 'ÃƒÂ©' | 'venceu' | 'inclui';
// KEYWORD : 'rei' | 'batalha' | 'primeiro' | 'descoberto' | 'Brasil' | 'terramoto' |
//         'famoso' | 'repÃƒÂºblica' | 'segunda' | 'maior' | 'primeira' | 'cidade' | 'serra' |
//         'mais' | 'alta' | 'regiÃ¯Â¿Â½o' | 'distrito' | 'Beja' | 'presidente' | 'liga' |
//         'futebol' | '2014/2015';

TEXTO:  '"' ~["]* '"';

NUMERO: DIGITO+;
PALAVRA: (LETRA)+;
fragment DIGITO: [0-9];
fragment LETRA: [a-zA-Z��];
// fragment LETRA: [a-zA-ZÃ¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½Ã¯Â¿Â½];
//fragment SIMBOLO: [-%$Ã¢â€šÂ¬@&()[\]{}=><+*;,Ã‚Âº~^/'"];
// fragment SIMBOLO: [-%$Ã¢â€šÂ¬@&()\[\]{}=><+*;,Ã‚ÂºÃ‚Âª~^/\'"];

SIMBOLOTERMINAL: [?.!];

SEPARADOR: ('\r'? '\n' | ' ' | '\t') -> skip;
// SEPARADOR: ('\r'? '\n' | ' ' | '\t') -> channel(HIDDEN);
