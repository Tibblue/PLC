<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output method="text"/>
    
    <xsl:template match="/">
        <xsl:apply-templates select="root/*"/>
        <xsl:apply-templates select="root/element/*"/>
    </xsl:template>
    
    <xsl:template match="root/*">
     
    ###  http://www.semanticweb.org/raulv/ontologies/2019/1/untitled-ontology-9#<xsl:value-of select="category"/><xsl:value-of select="year"/>
    :<xsl:value-of select="category"/><xsl:value-of select="year"/>
    rdf:type owl:NamedIndividual , :<xsl:value-of select="name(.)"/> ;
    
    <xsl:for-each select="laureates/element/id">
    :haslaureates  :r<xsl:value-of select="."/>;   
    </xsl:for-each>
        
    :category <xsl:value-of select="category"/>;
    :overallMotivation <xsl:value-of select="overallMotivation"/>;
    :year <xsl:value-of select="year"/>.
        
        
<!--    :firstname "<xsl:value-of select="firstname"/>" ;
    :id "<xsl:value-of select="id"/>" ;
    :motivation "<xsl:value-of select="motivation"/>" ;
    :share "<xsl:value-of select="share"/>" ;
    :surname "<xsl:value-of select="surname"/>" ;-->
      
    </xsl:template>
    
</xsl:stylesheet>