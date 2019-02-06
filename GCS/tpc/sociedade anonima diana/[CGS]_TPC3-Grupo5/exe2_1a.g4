grammar exe2_1a;

sociedade   : 'SA:' nomeEmpresa localizacao negocio capital ag socios administrador funcionarios
            ;

negocio     : 'NEGÓCIO:'ramo descricao
            ;

ramo        : 'ramo:' ( 'Agricultura' | 'Indústria' | 'Comércio') 
            ;

descricao   : 'descrição:' TEXTO
            ;

capital     : 'CAPITAL:' NUMERO moeda
            ;

moeda : '€' | '$' | '£'
            ;

ag          : 'DECISÕES APROVADAS EM AG:' decisao (';' decisao)*
            ;

decisao     : TEXTO
            ;

socios      : presidente maioritarios restoSocios
            ;

presidente  : 'PRESIDENTE:' socio
            ;

maioritarios : 'SÓCIOS MAIORITARIOS:' socio (';' socio)* 
             ;
             
restoSocios : 'SOCIOS:' socio (';' socio)* 
            ;

socio       :  nome ',' cota
            ;

nomeEmpresa : 'NOME:' TEXTO
            ;

localizacao : 'LOCALIZACAO:' TEXTO
            ;

cota        : PERCENT
            ;

administrador : 'ADMINISTRADOR:' nome estrategiasNegocio
              ;

nome : TEXTO
          ;

estrategiasNegocio : 'ESTRATÉGIAS DE NEGÓCIO:' estrategia (';' estrategia)*
                   ;

estrategia : TEXTO
           ;

funcionarios : gerente restoFuncionarios
             ;

gerente      : 'GERENTE:' funcionario
             ;

restoFuncionarios : 'FUNCIONARIOS:' funcionario (';' funcionario)* 
                  ;

funcionario  : id nomeFunc area dataNascimento dataServico contacto
             ;

nomeFunc: 'nome:' TEXTO
                 ;

dataNascimento : 'data de nascimento:' DATA
               ;

dataServico    : 'data de serviço:' DATA
               ;  

id           : 'id: ' IDENT 
             ;

contacto     : 'contacto:' NUMERO
             ;

area         : 'cargo:' ('producao' | 'escritorio' | 'armazem' | 'gerente')
             ;



/* Definicao do Analisador LEXICO */
IDENT : LETRA(LETRA|[0-9-_/])* ;

fragment LETRA : [a-zA-ZáéíóúÁÉÍÓÚÃãÕõâêôÂÊÔÀÈÌÒÙàèìòùÇç] ;

DATA : ('0'..'9')+'-'('0'..'9')+'-'('0'..'9')+ ;

TEXTO:    (('\''|'\"') ~('\''|'\"')* ('\''|'\"')); 

fragment DIGITO: [0-9];

PERCENT: ('100' | (DIGITO? DIGITO('.'DIGITO+)?))' '?'%';

NUMERO: ('0'..'9')+ ;

Separador: ('\r'? '\n' | ' ' | '\t')+  -> skip;
