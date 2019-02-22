<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">

    <xsl:output method="text"/>

    <xsl:template match="/">
        <xsl:apply-templates select="root/element"/>
        <xsl:apply-templates select="/*/*/*/element"/>
        <xsl:apply-templates select="root" mode="year"/>
    </xsl:template>

<!-- Primeira travessia - geral -->
    <xsl:template match="root/element">
        <xsl:variable name="idNobel">
            <xsl:value-of select="category"/><xsl:value-of select="year"/>
        </xsl:variable>
###  http://prc.di.uminho.pt/2019/tpc2#<xsl:value-of select="category"/><xsl:value-of select="year"/>
:<xsl:value-of select="category"/><xsl:value-of select="year"/> rdf:type owl:NamedIndividual , :<xsl:value-of select="concat(upper-case(substring(category,1,1)),substring(category,2))"/> ;
    <xsl:if test="overallMotivation">:overallMotivation <xsl:value-of select="overallMotivation"/> ;</xsl:if>
    :category "<xsl:value-of select="category"/>" ;
    :inYear :y<xsl:value-of select="year"/> ;
    :year <xsl:value-of select="year"/> .
    <xsl:for-each select="laureates/element">:<xsl:value-of select="$idNobel"/> :hasLaureate :l<xsl:value-of select="id"/> .
    </xsl:for-each>
    </xsl:template>
    
<!-- Segunda travessia - gerar Laureates -->
    <xsl:template match="element">
###  http://prc.di.uminho.pt/2019/tpc2#l<xsl:value-of select="id"/>
:l<xsl:value-of select="id"/> rdf:type owl:NameIndividual , :Laureates;
    :firstname "<xsl:value-of select="firstname"/>" ;
    :surname "<xsl:value-of select="surname"/>" ;
    <xsl:if test="motivation">:motivation <xsl:value-of select="motivation"/> ;</xsl:if>
    :id "<xsl:value-of select="id"/>" ;
    :share "<xsl:value-of select="share"/>" .
    </xsl:template>
    
<!-- Terceira travessia - gerar Laureates -->
    <xsl:template match="root" mode="year">  
####################
#       YEAR       #
####################
<!--        YEAR: <xsl:value-of select="year/text()"/>-->
<xsl:for-each select="distinct-values(/root/element/year/text())">
    ###  http://prc.di.uminho.pt/2019/tpc2#y<xsl:value-of select="."/>
    :y<xsl:value-of select="."/> rdf:type owl:NameIndividual , :Year.</xsl:for-each>
        
    </xsl:template>

</xsl:stylesheet>