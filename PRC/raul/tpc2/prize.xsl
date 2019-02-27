<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output method="text"/>
    
    <xsl:template match="/">
        <xsl:apply-templates select="root/*"/>
        <xsl:apply-templates select="root/element/laureates/element"/>
    </xsl:template>
    
    <xsl:template match="root/*">
     
    ###  http://www.semanticweb.org/raulv/ontologies/2019/1/untitled-ontology-9#<xsl:value-of select="category"/><xsl:value-of select="year"/>
    :<xsl:value-of select="category"/><xsl:value-of select="year"/>
    rdf:type owl:NamedIndividual , :Nobel ;
    
    <xsl:for-each select="laureates/element/id">
    :hasLaureates  :l<xsl:value-of select="."/>;   
    </xsl:for-each>
        
    :category "<xsl:value-of select="category"/>";
     <xsl:if test="overallMotivation">
         :overallMotivation <xsl:value-of select="overallMotivation"/>;
     </xsl:if>
    
    :year <xsl:value-of select="year"/>.
      
    </xsl:template>
    
    <xsl:template match="root/element/laureates/element">
        ###  http://www.semanticweb.org/raulv/ontologies/2019/1/untitled-ontology-9#l<xsl:value-of select="id"/>
        :l<xsl:value-of select="id"/>
        rdf:type owl:NamedIndividual , :Laureates ;
        
        :firstname "<xsl:value-of select="firstname"/>" ;
        :id "l<xsl:value-of select="id"/>" ;
        <xsl:if test="motivation">
            :motivation <xsl:value-of select="motivation"/>;
        </xsl:if>
        :share "<xsl:value-of select="share"/>" ;
        :surname "<xsl:value-of select="surname"/>" .
       </xsl:template>
    
    </xsl:stylesheet>