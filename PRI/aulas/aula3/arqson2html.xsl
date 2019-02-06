<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="2.0">
    
    
    <xsl:output method="html" indent="yes"/>
    
    <xsl:template match="/">
        <xsl:result-document href="arq-son/index.html">
            <html>
                <head>
                    <meta charset="UTF-8"/>
                </head>
                <body>
                    <h1>Arquivo Sonoro de Ernesto Veiga de Oliveira</h1>
                    <hr/>
                    <ul>
                        <xsl:apply-templates select="/arq/doc" mode="indice">
                            <xsl:sort select="tit"/>
                        </xsl:apply-templates>
                    </ul>
                </body>
            </html>
        </xsl:result-document>
        <xsl:apply-templates/>  <!-- Geraçao das paginas individuais -->
    </xsl:template>
    
    <xsl:template match="doc" mode="indice">
        <li>
            <a href="doc{count(preceding-sibling::*)+1}.html">
                <xsl:value-of select="tit"/>
            </a>
        </li>
    </xsl:template>
    
    <xsl:template match="doc">
        <xsl:result-document href="arq-son/doc{count(preceding-sibling::*)+1}.html">
            <html>
                <head>
                    <meta charset="UTF-8"/>
                </head>
                <body>
                    <h1><xsl:value-of select="tit"/></h1>
                    <hr/>
                    <table borber="1">
                        <tr>
                            <td>Provincia: </td><td><xsl:value-of select="prov"/></td>
                            <td>Local: </td><td><xsl:value-of select="local"/></td>
                            <td>Musico: </td><td><xsl:value-of select="musico"/></td>
                        </tr>
                    </table>
                    <p>[<a href="index.html">Voltar ao Indice</a>]</p>
                </body>
            </html>
        </xsl:result-document>
    </xsl:template>
    
    
    
</xsl:stylesheet>