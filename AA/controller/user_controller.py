
from flask import Blueprint, render_template, request, redirect, url_for
from lib.helper import render_result, render_err_result, course_data_path, user_data_path
from model.course import Course
from model.user import User
from model.user_admin import Admin
from model.user_instructor import Instructor
from model.user_student import Student

user_page = Blueprint("user_page", __name__)

model_user = User()
model_course = Course()
model_student = Student()


def generate_user(login_user_str):
    l = login_user_str.replace('\n','').split(';;;')
    login_user = User(int(l[0]),l[1],l[2],l[3],l[4]) # a User object
    return login_user


# use @user_page.route("") for each page url
@user_page.route("/login",methods=['GET'])
def login():
    return render_template('00login.html')
@user_page.route("/login",methods=['POST'])
def login_post():
    data = request.values
    username = data['username']
    password = data['password']
    if model_user.validate_username(username) and model_user.validate_password(password):
        flag,string_info = model_user.authenticate_user(username,password)
        if flag:
            User.current_login_user = generate_user(string_info)
        else:
            return render_err_result(msg='username or password error!')
    else:
        return render_err_result(msg='username or password not validate!')
    return render_result()
@user_page.route("/logout",methods=['GET'])
def logout():
    User.current_login_user = None
    return render_template('01index.html')
@user_page.route("/register",methods=['GET'])
def register():
    return render_template('00register.html')
@user_page.route("/register",methods=['POST'])
def register_post():
    data = request.values
    username = data['username']
    password = data['password']
    email = data['email']
    register_time = data['register_time']
    role = data['role']
    if model_user.validate_username(username) and model_user.validate_password(password) and model_user.validate_email(email):
        model_user.register_user(username,password,email,register_time,role)
        return render_result()
    else:
        return render_err_result(msg='username or password or email validate!')
@user_page.route("/student-list",methods=["GET"])
def student_list():
    if User.current_login_user:
        req = request.values
        page = req['page'] if "page" in req else 1
        page = int(page)
        context = {}
        # get values for one_page_instructor_list, total_pages, total_num
        one_page_student_list,total_pages,total_num = model_student.get_students_by_page(page)
        # get values for page_num_list
        page_num_list = model_course.generate_page_num_list(page,total_pages)
        # check one_page_instructor_list, make sure this variable not be None, if None, assign it to []
        if one_page_student_list == None:
            one_page_student_list = []

        context['one_page_student_list'] = one_page_student_list
        context['total_pages'] = total_pages
        context['page_num_list'] = page_num_list
        context['current_page'] = int(page)
        context['total_num'] = total_num
        # add "current_user_role" to context
        context['current_user_role'] = User.current_login_user.role

    else:
        return redirect(url_for("index_page.index"))

    return render_template("10student_list.html", **context)
@user_page.route("/student-info",methods=["GET"])
def student_info():
    if User.current_login_user:
        req = request.values
        student_id = req['id'] if "id" in req else -1
        context = {}
        context['current_user_role'] = User.current_login_user.role

        if student_id == -1:
            student = Student()
        else:
            student = model_student.get_student_by_id(student_id)
        context['student'] = student
        return render_template("11student_info.html", **context)

    else:
        return redirect(url_for("index_page.index"))

@user_page.route("/student-delete",methods=["GET"])
def student_delete():
    if User.current_login_user:
        req = request.values
        student_id = req['id']
        if model_student.delete_student_by_id(student_id):
            return redirect(url_for(user_page.student_list))
        else:
            redirect(url_for("index_page.index"))

    else:
        return redirect(url_for("index_page.index"))


