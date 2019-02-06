<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output encoding="UTF-8" method="html" indent="yes"/>
    
    <xsl:template match="/">
        <html>
            <head>
                <meta charset="UTF-8"/>
            </head>
            <body>
                <xsl:apply-templates/>
            </body>
        </html>
    </xsl:template>
    
    <xsl:template match="titulo">
        <h1><xsl:value-of select="."/></h1>
    </xsl:template>
    
    <xsl:template match="autor">
        <h2><xsl:value-of select="."/></h2>
    </xsl:template>
    
    <xsl:template match="data">
        <h3><xsl:value-of select="."/></h3>
    </xsl:template>
    
    <xsl:template match="quadra|terno">
        <p><xsl:apply-templates/></p>
    </xsl:template>
    
    <xsl:template match="verso">
        <xsl:apply-templates/>
        <br/>
    </xsl:template>
    
    <xsl:template match="nome">
        <span style="color:red"><xsl:value-of select="."/></span>
    </xsl:template>
    
    <xsl:template match="lugar">
        <span style="color:blue"><xsl:value-of select="."/></span>
    </xsl:template>
    
    


</xsl:stylesheet>
