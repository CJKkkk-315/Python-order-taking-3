# ------------      -------    --------    -----------    -----------
# @File       :  葡萄酒评论分析报告大作业模板.py    
# @Contact    :  河北农业大学
# @Copyright  :  信息科学与技术学院
# @Modify Time:  2022/4/22 
# @Version    :  1.0
# @License    : 仅限用于Python数据处理与分析大作业，具体要求请参照word文档。
# ------------      -------    --------    -----------    -----------

# 1 统计文件中出现的葡萄酒生产国家，输出不重复的国家名列表，按字母
#   表升序排序， 若国家名数据缺失，略过该条数据，返回值中不包含空字符串元素
# 2 计算每个国家的葡萄酒的平均得分，返回值为国家名和得分的列表
# 3 计算每个国家的葡萄酒的平均得分，返回值为国家名和得分的列表，按评分由高到低降序排列
# 4 评分最高的十款葡萄酒的编号、出产国、评分和价格，按评分降序输出
# 5 价格最高的二十款葡萄酒的编号、出产国、评分和价格，按价格降序输出
# 6 统计各个评分的葡萄酒数量是多少？输出包含评分和数量的列表
# 7 输出拥有葡萄酒数量最多的评分和数量
# 8 输出拥有葡萄酒数量最多的评分的葡萄酒的平均价格

import pandas as pd
import math

# 定义符号常量，用于索引，使之具有清晰的语义
NUMBER = 0
COUNTRY = 1
DESCRIPTION = 2
POINTS = 3
PRICE = 4
PROVINCE = 5


def csv_to_ls(file):
    """接收文件名为参数，逐行读取文件中的数据，根据逗号切分每行数据为列表类型，
    作为二维列表的一个元素，返回二维列表。
    @参数 file：文件名，字符串类型
    """
    wine_list = pd.read_csv(file).values.tolist()
    # print(wine_list)
    return wine_list


def country_ls(wine_list):
    """接收列表格式的葡萄酒数据为参数，略过标题行，返回不重复的国家名列表，按字母表升序排序，
    若国家名数据缺失，略过该条数据，返回值中不包含空字符串元素。
    @参数 wine_list：葡萄酒数据，列表类型
    """
    res = []
    for i in wine_list:
        if i[1] not in res and i[1]:
            res.append(i[1])
    res.sort()
    return res


def avg_point(wine_list, country):
    """接收列表格式的葡萄酒数据和国家名列表为参数，计算每个国家的葡萄酒的平均得分，
    返回值为国家名和得分的列表。
    @参数 wine_list：葡萄酒数据，列表类型
    @参数 country：国家名，列表类型
    """
    d = {i: [] for i in country}
    for i in wine_list:
        if i[1]:
            d[i[1]].append(i[3])
    res = []
    for i in d.keys():
        res.append([i, round(sum(d[i]) / len(d[i]), 2)])
    return res


def avg_point_sort(wine_list, country):
    """接收列表格式的葡萄酒数据和国家名列表为参数，计算每个国家的葡萄酒的平均得分，
    返回值为国家名和得分的列表，按评分由高到低降序排列。
    @参数 wine_list：葡萄酒数据，列表类型
    @参数 country：国家名，列表类型
    """
    d = {i: [] for i in country}
    for i in wine_list:
        if i[1]:
            d[i[1]].append(i[3])
    res = []
    for i in d.keys():
        res.append([i, round(sum(d[i]) / len(d[i]), 2)])
    res.sort(key=lambda x: x[1], reverse=True)
    return res

def top_10_point(wine_list):
    """接收列表格式的葡萄酒数据参数，返回评分最高的十款葡萄酒的编号、出产国、评分和价格，按评
    分降序输出。
    需要注意的是评分可能有缺失值，此时该数据为nan
    if math.isnan(x) == False可用于判定x的值是不是nan
    nan的数据类型是float,不可以直接用字符串判定方法。
    @参数 wine_list：葡萄酒数据，列表类型
    """
    wine_list.sort(key=lambda x: x[3], reverse=True)
    res = []
    for i in wine_list[:10]:
        res.append([i[0], i[1], i[3], i[4]])
    return res

def top_20_price(wine_list):
    """接收列表格式的葡萄酒数据参数，返回价格最高的二十款葡萄酒的编号、出产国、评分和价格，按价
    格降序输出。
    @参数 wine_list：葡萄酒数据，列表类型
    需要注意的是价格可能有缺失值，此时该数据为nan
    if math.isnan(x) == False可用于判定x的值是不是nan
    nan的数据类型是float,不可以直接用字符串判定方法。
    """
    wine_list = [i for i in wine_list if math.isnan(i[4]) == False]
    wine_list.sort(key=lambda x: x[4], reverse=True)
    res = []
    for i in wine_list[:20]:
        res.append([i[0], i[1], i[3], i[4]])
    return res


def amount_of_point(wine_list):
    """接收列表格式的葡萄酒数据参数，返回每个评分的葡萄酒数量，忽略没有评分的数据
    例如[...[84, 645], [85, 959],...]表示得分为84的葡萄酒645种，得分85的葡萄酒有959种。
    @参数 wine_list：葡萄酒数据，列表类型
    """
    wine_list = [i[3] for i in wine_list if math.isnan(i[3]) == False]
    d = {}
    for i in wine_list:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return sorted([[i, j] for i, j in d.items()], key=lambda x: x[0])


def most_of_point(amount_of_points):
    """接收每个评分的葡萄酒数量的列表为参数，返回获得该分数数量最多的评分和数量的列表。
    @参数 amount_of_points：每个评分的葡萄酒数量，列表类型
    """
    amount_of_points = sorted(amount_of_points, key=lambda x: x[1])
    return amount_of_points[-1]


def avg_price_of_most_point(wine_list, most_of_points):
    """接收列表格式的葡萄酒数据和获得最多的评分及数量的列表为参数
    忽略缺失价格的数据，返回这个分数的葡萄酒的平均价格，保留2位小数。
    @参数 wine_list：葡萄酒数据，列表类型
    @参数 most_of_points：获得最多的评分及数量，列表类型
    """
    s = 0
    n = 0
    for i in wine_list:
        if i[3] == most_of_points[0]:
            if math.isnan(i[4]) == False:
                s += i[4]
                n += 1
    return round(s/n,2)


if __name__ == '__main__':
    filename = 'winemag-data.csv'
    wine = csv_to_ls(filename)
    Country = country_ls(wine)
    print('国家名列表:')
    print(Country)
    print('每个国家的葡萄酒的平均得分:')
    print(avg_point(wine, Country))
    print('每个国家的葡萄酒的平均得分降序输出:')
    print(avg_point_sort(wine, Country))
    print('评分最高的十款葡萄酒的编号、出产国、评分和价格，按评分降序输出:')
    print(top_10_point(wine))
    print('价格最高的二十款葡萄酒的编号、出产国、评分和价格，按价格降序输出')
    print(top_20_price(wine))
    amount_point = amount_of_point(wine)
    print('各个评分的葡萄酒数量:')
    print(amount_point)
    Most_point = most_of_point(amount_point)
    print('拥有葡萄酒数量最多的评分和数量:')
    print(Most_point)
    print('拥有葡萄酒数量最多的评分的葡萄酒的平均价格:')
    print(avg_price_of_most_point(wine, Most_point))
