<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output method="text" encoding="UTF-8"/>
    
    <xsl:template match="/">
### DISTRITOS
        <xsl:for-each select="//distrito[not(designacao=preceding::designacao)]">
            <xsl:variable name="d" select="."/>
###  http://prc2018.di.uminho.pt/mapa#D<xsl:value-of select="generate-id(.)"/>
:D<xsl:value-of select="generate-id(.)"/> rdf:type owl:NamedIndividual ,
:Distrito ;
:nome "<xsl:value-of select="designacao"/>".
            <xsl:for-each select=".//concelho">
:D<xsl:value-of select="generate-id($d)"/> :temCidade :C<xsl:value-of select="generate-id(.)"/>.              
            </xsl:for-each>
            <xsl:call-template name="linha"/>
        </xsl:for-each>
        
### CIDADES
        <xsl:for-each select="//concelho[not(designacao=preceding::designacao)]">
###  http://prc2018.di.uminho.pt/mapa#C<xsl:value-of select="generate-id(.)"/>
:C<xsl:value-of select="generate-id(.)"/> rdf:type owl:NamedIndividual ,
:Cidade ;
:nome "<xsl:value-of select="designacao"/>";
:pertenceDistrito :D<xsl:value-of select="generate-id(../..)"/>.
            <xsl:call-template name="linha"/>
        </xsl:for-each>
    </xsl:template>
    
    <xsl:template name="linha">
        <xsl:text>
</xsl:text>
    </xsl:template>
</xsl:stylesheet>