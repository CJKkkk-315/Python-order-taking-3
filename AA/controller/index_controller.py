
from flask import render_template, Blueprint

from model.user import User
from model.user_admin import Admin

index_page = Blueprint("index_page", __name__)

@index_page.route("/",methods=['GET'])
def index():
    context = {}
    if User.current_login_user:
        context['current_user_role'] = User.current_login_user.role
    # manually register an admin account when open index page
    admin = Admin(username='admin',password='123456789')
    admin.register_admin()
    return render_template('01index.html',**context)



