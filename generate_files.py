# -*- coding: utf-8 -*-

import re
import codecs

regexp = re.compile('## \[(.*)\]\(([0-9]+)_0\.html\)')

question = """<meta charset="utf-8">
<link rel='stylesheet' href='markdown.css'/>
## {name}
[![{name}]({id}_0.jpg "{name}")]({id}_1.html)
"""

answer = """<meta charset="utf-8">
<link rel='stylesheet' href='markdown.css'/>
## {name}
[![{name}]({id}_1.jpg "{name}")](index.html)
"""

fi = codecs.open('index.md', encoding='utf-8')
for line in fi:
    a = regexp.match(line)
    if not a:
        print line, 
        continue
    num_id = a.group(2)
    str_id = a.group(1).encode('utf-8')
    with codecs.open(num_id+'_0.md', 'wb', encoding=None) as fo:
        fo.write(question.format(id = num_id, name = str_id))
    with codecs.open(num_id+'_1.md', 'wb', encoding=None) as fo:
        fo.write(answer.format(id = num_id, name = str_id))
