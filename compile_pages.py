import glob
import markdown
import bleach
import codecs

files = glob.glob('./*.md')
for name in files:
    name_out = name[:-3] + '.html'
    with codecs.open(name, encoding='utf-8') as fi:
        content = unicode(fi.read())
#        html = bleach.clean(markdown.markdown(content)).encode('utf-8')
        html = markdown.markdown(content).encode('utf-8')
        with codecs.open(name_out, 'wb', encoding=None) as fo:
            fo.write(html)

