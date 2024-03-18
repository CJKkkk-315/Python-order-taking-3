from docx import Document
import os
doc = Document('《景区管理》练习参考答案.docx')
s = []
res = []
title = 0
for para in doc.paragraphs:
    if para.text and para.text[0] == '#':
        if title:
            res.append([title,''.join(s)])
            s = []
            title = para.text
        else:
            title = para.text
    else:
        s.append(para.text + '\n')
res.append([title,''.join(s)])
print(res)
for i in res:
    name =  i[0].replace('#','')
    os.mkdir(name)
    with open('./' + name + '/' + name + '.txt', "w") as f:
        f.write(i[1])