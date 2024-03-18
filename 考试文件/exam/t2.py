from flask import Flask, render_template
# 导入pymysql库
import pymysql
# 导入DictCursor
from pymysql.cursors import 【游标对象代码】

# static_url_path参数配置静态资源的基础路径
# 此处需要手工配置静态资源和模板文件路径，因为没有使用默认命名


app = Flask(__name__, static_url_path='/css', static_folder='css', template_folder='template')

# 配置网站的首页路径（路由）, / 表示项目根路径
@app.route('/')
def t2():
    # 链接数据库
    conn = pymysql.connect(host=【本地数据库地址字符串】, port=【数据库连接端口号】, user=【访问数据库用户名】, password=【访问密码】,
                           database='exam', charset='utf8', autocommit=True)
    cursor = conn.cursor(【补充游标对象代码】)  # 执行任意SQL语句前均需要创建一个游标对象
    sql = "SELECT * FROM news" # 查询所有新闻信息
    cursor.execute(sql)  # 执行SQL语句
    result = cursor.【补充获得所有查询结果的代码】  # 从游标中返回全部结果，默认以(())二维元组保存
    return render_template("t2.html",result=【补充传递数据给前端的响应代码】)

# 将index.html作为模板页面被Flask渲染给浏览器
# return render_template('index.html')

if  __name__ == '__main__':
    app.run()