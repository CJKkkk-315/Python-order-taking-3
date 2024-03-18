from flask import Flask, render_template, request

from users import Users

app = Flask(__name__, static_url_path='/css', static_folder='css', template_folder='template')


@app.route('/')
def t3():
    return render_template("t3.html")

@app.route('/get')
def t3r():
    keyword = request.args.get("keyword")
    user_list = [] #保存所有的查询到包含关键字的用户
    print(keyword)
    for u in Users().find_by_name(keyword):
        user_list.append(u)
    print(user_list)
    return render_template("t3r.html", result=user_list)

if  __name__ == '__main__':
    app.run()