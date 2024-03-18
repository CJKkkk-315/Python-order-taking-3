# 按比例缩小图片尺寸
#将图片按修改时间排序(这样才能与图片的描述一致)，将路径存入列表，以便后面逐个插入图片时调用
import  os
from PIL import Image

for infile in ['0.png']:
    im = Image.open(infile)
    (x, y) = im.size  # 读取图片尺寸（像素）
    x_s = 600  # 定义缩小后的标准宽度
    y_s = 370  # 基于标准宽度计算缩小后的高度
    out = im.resize((x_s, y_s), Image.ANTIALIAS)  # 改变尺寸，保持图片高品质
    out.save(infile)
