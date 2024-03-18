# import os
# d = os.path.dirname(__file__)
# parent_path = os.path.dirname(d)
# course_data_path = parent_path + "/data/course.txt"
# user_data_path = parent_path + "/data/user.txt"
# course_json_files_path = parent_path + "/data/source_course_files"
# figure_save_path = parent_path + "/static/img/"
from lib.helper import course_data_path,user_data_path,course_json_files_path,figure_save_path
from .user import User
class Student(User):
    def __init__(self, uid=-1, username='', password='', register_time='yyyy-MM-dd  HH:mm:ss.SSS', role="student",
                 email=''):
        User.__init__(self, uid, username, password, register_time, role, )
        self.email = email

    def __str__(self):
        return f'{self.uid};;;{self.username};;;{self.password};;;{self.register_time};;;{self.role};;;{self.email}'

    def get_students_by_page(self,page):
        res = []
        aw = []
        n = 0
        with open(user_data_path, 'r',encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            l = i.replace('\n', '').split(';;;')
            if l[4] == 'student':
                n += 1
                aw.append(Student(*l))
                if len(aw) == 20:
                    res.append(aw[::])
                    aw = []
        if aw:
            res.append(aw)
        if res:
            return (res[page-1], len(res), n)
        else:
            return (None, len(res), n)
    def get_student_by_id(self,id):
        with open(user_data_path, 'r',encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            l = i.replace('\n', '').split(';;;')
            if l[4] == 'student' and l[0] == id:
                return Student(int(l[0]),l[1],l[2],l[3],l[4],l[5])

    def delete_student_by_id(self,id):
        flag = 0
        with open(user_data_path, 'r',encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            l = i.replace('\n', '').split(';;;')
            if l[4] == 'student' and l[0] == id:
                target = i
                flag = 1
        if flag:
            data.remove(target)
            with open(user_data_path, 'w',encoding='utf-8') as f:
                for i in data:
                    f.write(i)
            return True
        else:
            return False
