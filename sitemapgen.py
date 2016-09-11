import xml
import xml.etree.cElementTree as ET
from yattag import Doc, indent
import datetime
import pickle

doc, tag, text = Doc().tagtext()
lastmod = str(datetime.date.today())
print lastmod
with tag('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"):
        with tag('url'):
            with tag('loc'):
                text('http://www.zorya.co/')
            with tag('lastmod'):
                text(lastmod)
            with tag('changefreq'):
                text('weekly')
            with tag('priority'):
                text(1)
        with tag('url'):
            with tag('loc'):
                text('http://www.zorya.co/about/')
            with tag('lastmod'):
                text(lastmod)
            with tag('changefreq'):
                text('weekly')
            with tag('priority'):
                text(1)
        for x in range(1,32471):
                with tag('url'):
                    with tag('loc'):
                        text('http://www.zorya.co/object/%s' % x)
                    with tag('lastmod'):
                        text(lastmod)
                    with tag('changefreq'):
                        text('monthly')
                    with tag('priority'):
                        text(0.5)


result = indent(
    doc.getvalue(),
    indentation = ' '*4,
    newline = '\r\n'
)
file = open('static/sitemap.xml', 'w+')
file.write('<?xml version="1.0" encoding="UTF-8"?>' + doc.getvalue())
"""
<?xml version="1.0" encoding="UTF-8"?>

Dom = ET.parse('static/sitemap.xml')
urlset = ET.Element('urlset')
url = ET.SubElement(urlset,'url')
loc = ET.SubElement(url,'loc').
print ET.dump(urlset)

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>http://www.zorya.co/</loc>
      <lastmod>2015-12-07</lastmod>
      <changefreq>monthly</changefreq>
      <priority>1</priority>
   </url>
   """