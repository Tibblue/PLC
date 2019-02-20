<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">

    <xsl:output method="text"/>

    <xsl:template match="/">
        <xsl:apply-templates select="bibliography/*"/>
        <xsl:apply-templates select="//author|//editor"/>
    </xsl:template>

    <xsl:template match="bibliography/*">
        <xsl:variable name="idpub" select="@id"/>

        :<xsl:value-of select="@id"/>
            rdf:type owl:NamedIndividual , :<xsl:value-of select="name(.)"/> ;
            :title "<xsl:value-of select="title"/>" ;
            <xsl:if test="address">:address "<xsl:value-of select="address"/>";
            </xsl:if>
            <xsl:if test="month">:month "<xsl:value-of select="month"/>";
            </xsl:if>
            <xsl:if test="publisher">:publisher "<xsl:value-of select="publisher"/>";
            </xsl:if>
            <xsl:if test="booktitle">:booktitle "<xsl:value-of select="booktitle"/>";
            </xsl:if>
            <xsl:if test="chapter">:chapter "<xsl:value-of select="chapter"/>";
            </xsl:if>
            <xsl:if test="pages">:pages "<xsl:value-of select="pages"/>";
            </xsl:if>
            <xsl:if test="isbn">:isbn "<xsl:value-of select="isbn"/>";
            </xsl:if>
            <xsl:if test="howpublished">:howpublished "<xsl:value-of select="howpublished"/>";
            </xsl:if>
            <xsl:if test="issn">:issn "<xsl:value-of select="issn"/>";
            </xsl:if>
            <xsl:if test="journal">:journal "<xsl:value-of select="journal"/>";
            </xsl:if>
            <xsl:if test="school">:school "<xsl:value-of select="school"/>";
            </xsl:if>
            <xsl:if test="uri">:uri "<xsl:value-of select="uri"/>";
            </xsl:if>
            <xsl:if test="volume">:volume "<xsl:value-of select="volume"/>";
            </xsl:if>
            :doi "<xsl:value-of select="doi"/>" ;
            :year "<xsl:value-of select="year"/>" .


        <xsl:for-each select="author">
            :<xsl:value-of select="$idpub"/> :hasAutor :<xsl:value-of select="@id"/> .</xsl:for-each>
        <xsl:for-each select="editor">
            :<xsl:value-of select="$idpub"/> :hasEditor :<xsl:value-of select="@id"/> .</xsl:for-each>
        <xsl:for-each select="author-ref">
            :<xsl:value-of select="$idpub"/> :hasAutor :<xsl:value-of select="@authorid"/> .</xsl:for-each>
        <xsl:for-each select="editor-ref">
            :<xsl:value-of select="$idpub"/> :hasEditor :<xsl:value-of select="@authorid"/> .</xsl:for-each>

    </xsl:template>

    <xsl:template match="author">
        :<xsl:value-of select="@id"/> rdf:type owl:NameIndividual , :Author;
            :name "<xsl:value-of select="."/>" .
    </xsl:template>
    <xsl:template match="editor">
        :<xsl:value-of select="@id"/> rdf:type owl:NameIndividual , :Editor;
            :name "<xsl:value-of select="."/>" .
    </xsl:template>


</xsl:stylesheet>