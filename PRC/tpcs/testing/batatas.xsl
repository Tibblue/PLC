<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:foaf="http://xmlns.com/foaf/spec/"
    xmlns:jcr="http://www.di.uminho.pt/~jcr/prc2019#">
    
    <xsl:output method="xml" indent="yes"/>
    
    <xsl:template match="/">
        <rdf:RDF>
            <rdf:Description rdf:about="http://www.example.com/xml">
                <xsl:apply-templates/>
            </rdf:Description>
        </rdf:RDF>
    </xsl:template>

    <xsl:template match="person">
        <xsl:variable name="critic">
            <xsl:value-of select="name"/>
        </xsl:variable>
        <xsl:variable name="criticWebsite">
            <xsl:value-of select="website/@url"/>
        </xsl:variable>
        <jcr:hasCritic>
            <rdf:Description rdf:about="http://www.example.com/critic/{$critic}">
                <foaf:name>
                    <xsl:value-of select="name"/>
                </foaf:name>
                <foaf:homepage>
                    <rdf:Description rdf:about="http://{$criticWebsite}">
                        <rdfs:label>
                            <xsl:value-of select="website"/>
                        </rdfs:label>
                    </rdf:Description>
                </foaf:homepage>
            </rdf:Description>
        </jcr:hasCritic>
    </xsl:template>

    <!-- <xsl:template match="*">
    </xsl:template> -->

</xsl:stylesheet>
