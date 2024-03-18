from pyecharts.charts import *
from pyecharts import options as opts
from collections import Counter
with open('data.txt','r',encoding='utf8') as f:
    data = [i.replace('\n','').split(',') for i in f.readlines()]
zc = sorted(Counter([i[0] for i in data]).items(),key=lambda x:x[1],reverse=True)
x = [i[0] for i in zc]
y = [i[1] for i in zc]
pie = (
        Pie(init_opts=opts.InitOpts(width='1440px', height='800px'))
            .add(series_name='', data_pair=[(i, j) for i, j in zip(x, y)])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
pie.render('职称排名.html')


xs = sorted(Counter([i[1][0] for i in data]).items(),key=lambda x:x[1],reverse=True)
x = [i[0] for i in xs[:10]]
y = [i[1] for i in xs[:10]]
bar1 = (
        Bar()
            .add_xaxis(x)
            .add_yaxis("姓氏排名", y, yaxis_index=0, )
            .extend_axis(yaxis=opts.AxisOpts())
            .set_global_opts(title_opts=opts.TitleOpts(title="姓氏排名"))
    )
bar1.render('姓氏排名.html')


xl = sorted(Counter([i[4] for i in data]).items(),key=lambda x:x[1])
print(xl)
x = [i[0] for i in xl[:10]]
y = [i[1] for i in xl[:10]]
line = (
        Line()
        .add_xaxis(x)
        .add_yaxis('学历分布',y)
        .set_global_opts(title_opts=opts.TitleOpts('学历分布'))
    )
line.render('学历分布.html')

