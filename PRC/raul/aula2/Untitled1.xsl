<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output method="text" indent="yes"/>
    
    <xsl:template match="/">
        <xsl:apply-templates select="bibliography/*"/>
        <xsl:apply-templates select="//author|//editor"/>
    </xsl:template>
    
    <xsl:template match="bibliography/*">
        <xsl:variable name="idpub" select="@id"/>
        
        ###  http://prc.di.uminho.pt/2019/pubs# <xsl:value-of select="@id"/>
        :<xsl:value-of select="$idpub"/> rdf:type owl:NamedIndividual ,
                : <xsl:value-of select="name(.)"/>
            : address<xsl:value-of select="address"/>;
            : year <xsl:value-of select="year"/>
            : title <xsl:value-of select="title"/> 
        
        <xsl:for-each select="author">
            :<xsl:value-of select="$idpub"/> :hasAuthor: <xsl:value-of select="@id"/> .
        </xsl:for-each>
        
        <xsl:for-each select="editor">
            :<xsl:value-of select="$idpub"/> :hasEditor: <xsl:value-of select="@id"/> .
        </xsl:for-each>
        
        <xsl:for-each select="author-ref">
            :<xsl:value-of select="$idpub"/> :hasAuthor: <xsl:value-of select="@authorid"/> .
        </xsl:for-each><xsl:for-each select="author">
            
        <xsl:for-each select="editor-ref">
            :<xsl:value-of select="$idpub"/> :hasEditor: <xsl:value-of select="@authorid"/> .
        </xsl:for-each>
    
    <xsl:template match="author">
        :<xsl:value-of select="@id"/> rdf:type owl:NamedIndividual .
                                      :Author ;
        :name " <xsl:value-of select="."/>

        <xsl:template match="editor">
            :<xsl:value-of select="@id"/> rdf:type owl:NamedIndividual .
                                          :Author ;
            :name " <xsl:value-of select="."/>
    </xsl:template>
    
    
    
    
    
</xsl:stylesheet>