import os
import sys
import re
import chardet

# 扫描文件夹下面所有的文件，并保存在文件目录备份表中
path = 'STNO-UNICODE'
new_path = 'TXT'


def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):  # 如果是文件则添加进 fileList
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):  # 如果是文件夹
            newDir = os.path.join(dir, s)
            GetFileList(newDir, fileList)
    return fileList


# 主函数
# 重定向输出位置
output = sys.stdout
outputfile = open('path.txt', 'w')
sys.stdout = outputfile
list = GetFileList(path, [])  # 获取所有myFolder文件夹下所有文件名称（包含拓展名）
# 输出所有文件夹中的路径（相对于当前运行的.py文件的相对路径）
for route in list:
    # route 为路径
    print(route)
# 关闭输出重定向
outputfile.close()
sys.stdout = output

# 将生成的路径文件path.txt读取，并按照路径文件对文本处理，去标签
for line in open("path.txt"):
    line = line.strip()
    fb = open(line, "rb")
    data = fb.read()
    encoding = chardet.detect(data)['encoding']  # 获取当前文件的编码方式，并按照此编码类型处理文档
    print(encoding)
    text = open(line, 'r', encoding=encoding).read()
    pattern = re.compile(r'<[^>]+>', re.S)  # 去HTML标签
    result = pattern.sub('', text)
    # print(dd)
    name = line.split('\\')[-1].split('.')[0]
    fname = 'TXT' + "\\" + name + ".txt"
    # print(fname)
    f = open(fname, "w+", encoding=encoding)  # 将去标签的文件写到文件夹内，并按照原命名以txt文档方式保存
    # fo=open(fname,"w+")
    f.write(result)

    output = sys.stdout
    outputfile = open('new_path.txt', 'w')
    sys.stdout = outputfile
    list = GetFileList(new_path, [])  # 获取所有myFolder文件夹下所有文件名称（包含拓展名）
    # 输出所有文件夹中的路径（相对于当前运行的.py文件的相对路径）
    for route in list:
        # route 为路径
        print(route)
    # 关闭输出重定向
    outputfile.close()
    sys.stdout = output
