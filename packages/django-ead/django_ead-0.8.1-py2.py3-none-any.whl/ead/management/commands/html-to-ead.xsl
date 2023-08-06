<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
                xmlns:ead="http://ead3.archivists.org/schema/"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <!-- Convert XHTML, annotated with attributes used to express the
       original EAD3 elements and attributes (see ead-to-html.xsl), to
       EAD3 XML. -->

  <xsl:output encoding="utf-8"/>

  <xsl:template match="wrapper">
    <wrapper>
      <xsl:apply-templates/>
    </wrapper>
  </xsl:template>

  <xsl:template match="*">
    <xsl:element name="ead:{substring-after(@class, 'ead-')}">
      <xsl:apply-templates select="@*[starts-with(local-name(), 'data-ead-')]"/>
      <xsl:apply-templates/>
    </xsl:element>
  </xsl:template>

  <xsl:template match="@*">
    <xsl:attribute name="{substring-after(local-name(), 'data-ead-')}">
      <xsl:value-of select="."/>
    </xsl:attribute>
  </xsl:template>

</xsl:stylesheet>
