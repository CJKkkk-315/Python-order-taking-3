import os
import json
from user import User
import lib.helper as helper
class Instructor:
    def __init__(self, uid=-1, username: str = "", password: str = "", register_time: str = 'yyyy-MM-dd_HH:mm:ss.SSS', role: str = "",
                 email: str = "", display_name: str = "", job_title: str = "", course_id_list: list = []):
        self.uid = uid
        self.username = username
        self.password = password
        self.register_time = register_time
        self.role = role
        self.email = email
        self.display_name = display_name
        self.job_title = job_title
        self.course_id_list = course_id_list


    def __str__(self):
        return str(';;;'.join([str(i) for i in [self.uid, self.username, self.password, self.register_time, self.role, self.email, self.display_name, self.job_title, '--'.join(self.course_id_list)]]))


    def get_instructors(self):
        u = User()
        instructors_dict = {}
        instructor_register_time = 'xx-xx-xxxx'
        role = 'instructor'

        with open('./' + 'data/user.txt', 'r', encoding='ut-8') as load_instructor:
            for f in load_instructor.readlines():
                instructor = f.strip().split(';;;')
                instructor[-1]= instructor[-1].split('--')
                instructors_dict[int(instructor[0])] = instructor

        source_path = [i for i in os.listdir('./' + 'data/source_course_files')
                       if not i.startswith('.')]
        for folder in source_path:
            course_path = '.' + 'data/source_course_files' + '/' + folder
            course_folder = [i for i in os.listdir(course_path) if not i.startswith('.')]
            for course_name in course_folder:
                courses = os.listdir(course_path + '/' + course_name)
                for course_item_name in courses:
                    item_path = course_path + '/' + course_name + '/' + course_item_name
                    with open(item_path, 'r', encoding='utf-8') as course_items:
                        items = json.loads(course_items.readline())
                        for item in items['unit_info']['items']:
                            course_id = str(item['id'])
                            for instructor in item['visible_instructors']:
                                instructor_id = instructor['id']
                                if instructor_id in instructors_dict.keys():
                                    instructors_dict[instructor_id][1].append(course_id)
                                    continue
                                else:
                                    instrutor_display_name = instructor['display_name']
                                    instructor_username = instrutor_display_name.lower.replace('','_')
                                    instructor_password = instructor_id
                                    instructor_email = instructor_username + '@gmail.com'
                                    instructor_job_title = instructor['job_title']
                                    instructors_dict[instructor_id] = [instructor_id, instructor_username, u.encrypt_password(instructor_password), instructor_register_time, role, instructor_email, instrutor_display_name, instructor_job_title, [course_id]]

        with open('./'+'data/user.txt', 'w', encoding='utf-8') as instructor_write:
            for value in instructors_dict.values():
                value[-1] = '--'.join(list(set(value[-1])))
                instructor_write.write(';;;'.join([str(i) for i in value]))
                instructor_write.write('\n')





    def get_instructors_by_page(self):
        pass

    def generate_instructor_figure1(self):
        pass
# if __name__=='__main--':
#     ins = Instructor()
#     ins.get_instructors()

