<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:html="http://www.w3.org/1999/xhtml"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:jcr="http://www.di.uminho.pt/~jcr/prc2019#"
    xmlns:base="http://www.di.uminho.pt/~jcr/prc2019#">
    
    <xsl:output method="xml" indent="yes"/>
    
    <xsl:template match="/">
        <rdf:RDF>
            
            <rdfs:Class rdf:about="http://www.di.uminho.pt/~jcr/prc2019#Book"/>
            <rdfs:Class rdf:about="http://www.di.uminho.pt/~jcr/prc2019#Inbook"/>
            <rdf:Property rdf:about="http://www.di.uminho.pt/~jcr/prc2019#author-ref">
                <rdfs:domain rdf:resource="http://www.di.uminho.pt/~jcr/prc2019#Inbook"/>
                <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
            </rdf:Property>
            <rdf:Property rdf:about="http://www.di.uminho.pt/~jcr/prc2019#editor-ref">
                <rdfs:domain rdf:resource="http://www.di.uminho.pt/~jcr/prc2019#Inbook"/>
                <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
            </rdf:Property>
            <rdf:Property rdf:about="http://www.di.uminho.pt/~jcr/prc2019#editor">
                <rdfs:domain rdf:resource="http://www.di.uminho.pt/~jcr/prc2019#Inbook"/>
                <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
            </rdf:Property>
            <rdf:Property rdf:about="http://www.di.uminho.pt/~jcr/prc2019#title">
                <rdfs:domain rdf:resource="http://www.di.uminho.pt/~jcr/prc2019#Inbook"/>
                <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
            </rdf:Property>
            <rdfs:Class rdf:about="http://www.di.uminho.pt/~jcr/prc2019#Proceedings"/>
            <rdfs:Class rdf:about="http://www.di.uminho.pt/~jcr/prc2019#Inproceedings"/>
            <rdfs:Class rdf:about="http://www.di.uminho.pt/~jcr/prc2019#Article"/>
            <rdfs:Class rdf:about="http://www.di.uminho.pt/~jcr/prc2019#Misc"/>
            <rdfs:Class rdf:about="http://www.di.uminho.pt/~jcr/prc2019#Phdthesis"/>
            <rdfs:Class rdf:about="http://www.di.uminho.pt/~jcr/prc2019#Masterthesis"/>
            
            <rdf:Description rdf:about="http://www.di.uminho.pt/~jcr/prc2019">
                <xsl:apply-templates/>
            </rdf:Description>
        </rdf:RDF>
    </xsl:template>
    
    <xsl:template match="inbook">
        <jcr:inbook>
            <rdfs:Class rdf:ID="{@id}">
                <xsl:for-each select="author-ref">
                    <jcr:author-ref>
                        <xsl:value-of select="@authorid"/>
                    </jcr:author-ref>
                </xsl:for-each>
                <xsl:for-each select="editor-ref">
                    <jcr:editor-ref>
                        <xsl:value-of select="@authorid"/>
                    </jcr:editor-ref>
                </xsl:for-each>
                <xsl:for-each select="editor">
<!--                    <jcr:editor jcr:id="{@id}">-->
                    <jcr:editor>
                        <xsl:value-of select="."/>
                    </jcr:editor>
                </xsl:for-each>
                
                
                <jcr:title>
<!--                    <xsl:value-of select="name(.)"/>-->
                    <xsl:value-of select="title"/>
                </jcr:title>
            </rdfs:Class>
        </jcr:inbook>
    </xsl:template>
    
    <xsl:template match="text()" priority="-1"/>
    
</xsl:stylesheet>