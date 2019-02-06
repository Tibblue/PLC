<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="2.0">
    
    <xsl:output method="html" indent="yes"/>
    
    <xsl:template match="/">
        <xsl:result-document href="website/index.html">
            <html>
                <head>
                    <meta charset="UTF-8"/>
                </head>
                <body>
                    <xsl:apply-templates mode="index"/>
                </body>
            </html>
        </xsl:result-document>
        <xsl:apply-templates mode="sura"/>  <!-- Geraçao das paginas individuais -->
    </xsl:template>
    
    <!-- Templates do conteudo do index -->
    <xsl:template match="tstmt" mode="index">
        <xsl:apply-templates mode="index"/>
    </xsl:template>
    
    <xsl:template match="coverpg" mode="index">
        <h1 align="center"><xsl:value-of select="title"/></h1>
        <h2 align="center"><xsl:value-of select="title2"/></h2>
        <hr/>
        <xsl:apply-templates mode="index"/>
    </xsl:template>
    
    <xsl:template match="titlepg" mode="index">
        <h4><i><xsl:value-of select="subtitle/p"/></i></h4>
    </xsl:template>
    
    <xsl:template match="preface" mode="index">
        <h3><xsl:value-of select="ptitle"/></h3>
        <xsl:apply-templates mode="index"/>
    </xsl:template>
    
    <xsl:template match="p" mode="index">
        <p><xsl:value-of select="."/></p>
    </xsl:template>
    
    <xsl:template match="suracoll" mode="index">
        <h2>Indice: </h2>
        <ul>
            <xsl:apply-templates mode="indice"/>
            <!-- Gerar o indice -->
        </ul>
    </xsl:template>
    
    <xsl:template match="text()" mode="index" priority="-1"/>
    
    <!-- Templates para indice -->
    <xsl:template match="sura" mode="indice">
        <li>
            <a href="sura{count(preceding-sibling::*)+1}.html">
                <xsl:value-of select="bktlong"/>
            </a>
        </li>
    </xsl:template>
    
    <xsl:template match="text()" mode="indice" priority="-1"/>
    
    <!-- Templates das paginas individuais -->
    <xsl:template match="sura" mode="sura">
        <xsl:result-document href="website/sura{count(preceding-sibling::*)+1}.html">
            <html>
                <head>
                    <meta charset="UTF-8"/>
                </head>
                <body>
                    <h1 align="center"><xsl:value-of select="bktshort"/></h1>
                    <h3 align="center"><xsl:value-of select="epigraph"/></h3>
                    <hr/>
                    <h2><xsl:value-of select="bktlong"/></h2>
                    <xsl:apply-templates mode="sura"/>
                    <hr/>
                    <p>[<a href="index.html">Voltar ao Indice</a>]</p>
                </body>
            </html>
        </xsl:result-document>
    </xsl:template>
    
    <xsl:template match="v" mode="sura">
        <p><xsl:value-of select="."/></p>
    </xsl:template>
    
    <xsl:template match="text()" mode="sura" priority="-1"/>
    
    
    
    
</xsl:stylesheet>