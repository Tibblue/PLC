<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">

    <xsl:output method="text"/>

    <xsl:template match="/">
        <xsl:apply-templates select="root/*"/>
        <xsl:apply-templates select="/*/*/*/element"/>
    </xsl:template>

    <xsl:template match="root/*">
        <xsl:variable name="idNobel">
            <xsl:value-of select="category"/><xsl:value-of select="year"/>
        </xsl:variable>
        
###  http://prc.di.uminho.pt/2019/tpc2#<xsl:value-of select="category"/><xsl:value-of select="year"/>
:<xsl:value-of select="category"/><xsl:value-of select="year"/> rdf:type owl:NamedIndividual , :Nobel ;
    <xsl:if test="overallMotivation">:overallMotivation <xsl:value-of select="overallMotivation"/> ;</xsl:if>
    :category "<xsl:value-of select="category"/>" ;
    :year <xsl:value-of select="year"/> .
        
    <xsl:for-each select="laureates/element">:<xsl:value-of select="$idNobel"/> :hasLaureate :l<xsl:value-of select="id"/> .
    </xsl:for-each>

    </xsl:template>

    <xsl:template match="element">
        
:l<xsl:value-of select="id"/> rdf:type owl:NameIndividual , :Laureates;
    :firstname "<xsl:value-of select="firstname"/>" ;
    :surname "<xsl:value-of select="surname"/>" ;
    <xsl:if test="motivation">:motivation <xsl:value-of select="motivation"/> ;</xsl:if>
    :id "<xsl:value-of select="id"/>" ;
    :share "<xsl:value-of select="share"/>" .
        
    </xsl:template>


</xsl:stylesheet>