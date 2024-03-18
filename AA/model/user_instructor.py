import os
import matplotlib.pyplot as plt
# d = os.path.dirname(__file__)
# parent_path = os.path.dirname(d)
# course_data_path = parent_path + "/data/course.txt"
# user_data_path = parent_path + "/data/user.txt"
# course_json_files_path = parent_path + "/data/source_course_files"
# figure_save_path = parent_path + "/static/img/"
from lib.helper import course_data_path,user_data_path,course_json_files_path,figure_save_path
from collections import defaultdict
from .user import User
import json
class Instructor(User):
    def __init__(self,uid=-1,username='',password='',register_time='yyyy-MM-dd  HH:mm:ss.SSS',role="instructor",
                 email='',display_name='',job_title='',course_id_list=[]):
        User.__init__(self,uid,username,password,register_time,role,)
        self.display_name = display_name
        self.email = email
        self.job_title = job_title
        self.course_id_list = course_id_list

    def __str__(self):
        return f'{self.uid};;;{self.username};;;{self.password};;;{self.register_time};;;{self.role};;;{self.email};;;{self.display_name};;;{self.job_title};;;{"--".join(self.course_id_list)}'

    def get_instructors(self):
        d = defaultdict(list)
        res = []
        ids = []
        def SearchFiles(directory):
            fileList = []
            for root, subDirs, files in os.walk(directory):
                for fileName in files:
                    fileList.append(os.path.join(root, fileName))
            return fileList

        for dir in os.listdir(course_json_files_path):
            directory = course_json_files_path + '\\' + dir
            fileList = SearchFiles(directory)
            for file in fileList:
                with open(file, 'r') as f:
                    js = json.load(f)
                    for course in js['unitinfo']['items']:
                        for i in course['visible_instructors']:
                            d[i['id']].append(course['id'])
                            if i['id'] not in ids:
                                ids.append(i['id'])
                                res.append([i['id'],i['display_name'].lower().replace(' ','_'),User.encrypt_password(i['id']),'yyyy-MM-dd  HH:mm:ss.SSS','instructor',i['display_name'].lower().replace(' ','_')+'@gmail.com',i['display_name'],i['job_title']])
        with open(user_data_path, 'w', encoding='utf-8') as f:
            for i in res:
                f.write(';;;'.join(list(map(str, i)))+';;;'+'--'.join(list(map(str,d[i[0]])))+'\n')


    def get_instructors_by_page(self,page):
        res = []
        aw = []
        n = 0
        with open(user_data_path, 'r',encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            l = i.replace('\n', '').split(';;;')
            if l[4] == 'instructor':
                n += 1
                aw.append(Instructor(*l))
                if len(aw) == 20:
                    res.append(aw[::])
                    aw = []
        if aw:
            res.append(aw)
        if res:
            return (res[page - 1], len(res), n)
        else:
            return (None, len(res), n)


    def generate_instructor_figure1(self):
        plt.clf()
        with open(user_data_path, 'r', encoding='utf-8') as f:
            data = f.readlines()
        res = []
        for i in data:
            l = i.replace('\n','').split(';;;')
            p = Instructor(*l)
            res.append([p.job_title,len(p.course_id_list)])
        res.sort(key=lambda x:x[1],reverse=True)
        x = [' '.join(i[0].split()[:3]) for i in res[:10]]
        y = [i[1] for i in res[:10]]
        plt.bar(x,y)
        plt.xticks(fontsize=7,rotation=45)
        plt.savefig(figure_save_path+'instructor_figure1.png')
        return 'Teacher model worker'