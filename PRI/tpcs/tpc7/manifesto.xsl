<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output method="html" indent="yes"/>
    
    <xsl:template match="/">
        <h1 align="center">Project Record</h1>
        <hr/>
        <xsl:apply-templates/>
    </xsl:template>

    <xsl:template match="meta">
        <table width="100%">
            <tr>
                <td width="66%">
                    <p style="font-size:24px">
                      <b>Chave: </b>
                      <xsl:value-of select="id"/>
                    </p>
                    <p style="font-size:24px">
                      <b>Título: </b>
                      <xsl:value-of select="título"/>
                    </p>
                    <xsl:if test="subtítulo!=''">
                      <p style="font-size:20px">
                          <b>Subtítulo: </b>
                          <xsl:value-of select="subtítulo"/>
                      </p>
                    </xsl:if>
                    <p style="font-size:20px">
                        <b>Supervisor: </b>            
                        <xsl:if test="supervisor/website!=''">
                            <a href="{supervisor/website}">
                                <xsl:value-of select="supervisor/nome"/>
                            </a>
                        </xsl:if>
                        <xsl:if test="supervisor/website=''">
                            <xsl:value-of select="supervisor/nome"/>
                        </xsl:if>
                        - 
                        <a href="mailto:{supervisor/email}">
                            <xsl:value-of select="supervisor/email"/>
                        </a>
                    </p>
                </td>
                <td align="right" valign="top">
                    <xsl:if test="dinício!=''">
                        <p style="font-size:16px">
                            <b>Data de Início: </b>
                            <xsl:value-of select="dinício"/>
                        </p>
                    </xsl:if>
                    <p style="font-size:16px">
                        <b>Data de Fim: </b>
                        <xsl:value-of select="dfim"/>
                    </p>
                </td>
            </tr>
        </table>
        <hr/>
    </xsl:template>
    
    <xsl:template match="equipe">
        <ol>
            <xsl:apply-templates/>
        </ol>
        <hr/>
    </xsl:template>
    <xsl:template match="elemento">
        <table>
            <tr>
                <th>
                    <li style="align:center">
                    <xsl:if test="website!=''">
                       <a href="{website}">
                           <xsl:value-of select="nome"/>
                       </a>
                    </xsl:if>
                    <xsl:if test="website=''">
                       <xsl:value-of select="nome"/>
                    </xsl:if>
                    <br/>
                    <a href="mailto:{email}">
                       <xsl:value-of select="email"/>
                    </a>
                    </li>
                </th>
                <th>
                    <xsl:if test="foto/@path!=''">
                        <img style="height:96px" align="right"
                            src="{foto/@path}" alt="foto"/>
                    </xsl:if>
                </th>
            </tr>
        </table>
        
    </xsl:template>
    
    <xsl:template match="resumo">
        <p style="font-size:24px">
            <b>Resumo</b>
        </p>
        <xsl:apply-templates/>
    </xsl:template>
    <xsl:template match="para">
        <p>
            <xsl:apply-templates/>
        </p>
    </xsl:template>
    <xsl:template match="b">
        <b>
            <xsl:apply-templates/>
        </b>
    </xsl:template>
    <xsl:template match="i">
        <i>
            <xsl:apply-templates/>
        </i>
    </xsl:template>
    
    <xsl:template match="resultados">
        <hr/>
        <p style="font-size:24px">
            <b>Resultados</b>
        </p>
        <ul>
            <xsl:apply-templates/>
        </ul>
    </xsl:template>
    <xsl:template match="resultado">
        <li>
            <a href="{@path}">
                <xsl:value-of select="."/>
            </a>
        </li>
    </xsl:template>
    
    
</xsl:stylesheet>