<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
                xmlns:ead="http://ead3.archivists.org/schema/"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <!-- Convert EAD3 XML into XHTML, with attributes used to express
       the original EAD3 elements and attributes to allow for
       conversion back into EAD3. -->

  <xsl:output encoding="utf-8"/>

  <xsl:template match="ead:abbr">
    <xsl:call-template name="ead-element-in-html">
      <xsl:with-param name="element" select="'abbr'"/>
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="ead:abbr/@expan">
    <xsl:attribute name="title">
      <xsl:value-of select="."/>
    </xsl:attribute>
  </xsl:template>

  <xsl:template match="ead:blockquote">
    <xsl:call-template name="ead-element-in-html">
      <xsl:with-param name="element" select="'blockquote'"/>
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="ead:emph">
    <xsl:call-template name="ead-element-in-html">
      <xsl:with-param name="element" select="'em'"/>
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="ead:item">
    <xsl:call-template name="ead-element-in-html">
      <xsl:with-param name="element" select="'li'"/>
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="ead:lb">
    <xsl:call-template name="ead-element-in-html">
      <xsl:with-param name="element" select="'br'"/>
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="ead:list">
    <xsl:call-template name="ead-element-in-html">
      <xsl:with-param name="element" select="'ul'"/>
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="ead:list[@listtype='ordered']">
    <xsl:call-template name="ead-element-in-html">
      <xsl:with-param name="element" select="'ol'"/>
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="ead:p">
    <xsl:call-template name="ead-element-in-html">
      <xsl:with-param name="element" select="'p'"/>
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="ead:quote">
    <xsl:call-template name="ead-element-in-html">
      <xsl:with-param name="element" select="'q'"/>
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="ead:ref[@href]">
    <xsl:call-template name="ead-element-in-html">
      <xsl:with-param name="element" select="'a'"/>
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="ead:ref/@href">
    <xsl:copy-of select="."/>
  </xsl:template>

  <xsl:template match="ead:*">
    <xsl:call-template name="ead-element-in-html"/>
  </xsl:template>

  <xsl:template match="@lang">
    <xsl:attribute name="xml:lang">
      <xsl:value-of select="."/>
    </xsl:attribute>
  </xsl:template>

  <xsl:template match="@*"/>

  <xsl:template match="ead:*" mode="ead-as-attribute">
    <xsl:attribute name="class">
      <xsl:value-of select="concat('ead-', local-name())"/>
    </xsl:attribute>
  </xsl:template>

  <xsl:template match="@*" mode="ead-as-attribute">
    <xsl:attribute name="{concat('data-ead-', local-name())}">
      <xsl:value-of select="."/>
    </xsl:attribute>
  </xsl:template>

  <xsl:template name="ead-element-in-html">
    <xsl:param name="element" select="'span'"/>
    <xsl:element name="{$element}">
      <xsl:apply-templates mode="ead-as-attribute" select="."/>
      <xsl:apply-templates mode="ead-as-attribute" select="@*"/>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:element>
  </xsl:template>

</xsl:stylesheet>
