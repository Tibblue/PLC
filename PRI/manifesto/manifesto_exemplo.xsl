<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output method="html" indent="yes"/>
    
    <xsl:template match="/">
        <xsl:apply-templates/>
    </xsl:template>

    <xsl:template match="supervisor">
        <p>
            <a href="{website}">
                <xsl:value-of select="nome"/>
            </a>
            <br/>
            <a href="mailto:{email}">
                Enviar correio
            </a>
        </p>
    </xsl:template>
    
    
    
</xsl:stylesheet>