<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="2.0">
    
    <xsl:output method="text" indent="yes"/>
    
    <xsl:template match="obra">
        <xsl:result-document href="website/json/obre{@id}.json">
            {"id": "<xsl:value-of select="@id"/>",
             "titulo": "<xsl:value-of select="titulo"/>",
             "tipo": "<xsl:value-of select="tipo"/>"
            <xsl:if test="compositor">
                , "compositor": "<xsl:value-of select="compositor"/>"
            </xsl:if>
            <xsl:if test="arranjo">
                , "arranjo": "<xsl:value-of select="arranjo"/>"
            </xsl:if>
            <xsl:if test="instrumentos/instrumento">
                , "instrumentos": [
                <xsl:for-each select="instrumentos/instrumento">
                    {
                    "designaçao": "<xsl:value-of select="designacao"/>",
                    <xsl:if test="partitura/@afinacao">
                        "afinaçao": "<xsl:value-of select="partitura/@afinacao"/>",
                    </xsl:if>
                    <xsl:if test="partitura/@voz">
                        "voz": "<xsl:value-of select="partitura/@voz"/>",
                    </xsl:if>
                    <xsl:if test="partitura/@clave">
                        "clave": "<xsl:value-of select="partitura/@clave"/>",
                    </xsl:if>
                    "path": "<xsl:value-of select="partitura/@path"/>"
                    }
                    <xsl:if test="following-sibling::*">,</xsl:if>
                </xsl:for-each>
                ]
            </xsl:if>
            }
        </xsl:result-document>
    </xsl:template>
    
    
</xsl:stylesheet>