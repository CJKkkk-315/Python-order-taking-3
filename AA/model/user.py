import os
from lib.helper import course_data_path,user_data_path,course_json_files_path,figure_save_path
# d = os.path.dirname(__file__)
# parent_path = os.path.dirname(d)
# course_data_path = parent_path + "/data/course.txt"
# user_data_path = parent_path + "/data/user.txt"
# course_json_files_path = parent_path + "/data/source_course_files"
# figure_save_path = parent_path + "/static/img/"
import random
class User:
    current_login_user = None
    def __init__(self,uid = -1,username = '',password = '',register_time = 'yyyy-MM-dd  HH:mm:ss.SSS',role = '',):
        self.uid = int(uid)
        self.username = username
        self.password = password
        self.register_time = register_time
        self.role = role

    def __str__(self):
        return f'{self.uid};;;{self.username};;;{self.password};;;{self.register_time};;;{self.role}'

    def validate_username(self, username):
        for i in username:
            if i.isalpha() or i == '_':
                continue
            else:
                return False
        return True

    def validate_password(self, password):
        if len(password) < 8:
            return False
        return True

    def validate_email(self, email):
        if '@' not in email or email[-4:] != '.com' or len(email) <= 8:
            return False
        else:
            return True
    def clear_user_data(self):
        file = open(user_data_path, 'w').close()

    def authenticate_user(self, username, password):
        with open(user_data_path,'r',encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            l = i.replace('\n','').split(';;;')
            if username == l[1] and self.encrypt_password(password) == l[2]:
                return (True,str(i))
        return (False,"")

    def check_username_exist(self, username):
        with open(user_data_path, 'r',encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            l = i.replace('\n', '').split(';;;')
            if username == l[1]:
                return True
        return False

    def generate_unique_user_id(self):
        e = []
        with open(user_data_path, 'r',encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            l = i.replace('\n', '').split(';;;')
            e.append(l[0])
        while True:
            num = str(random.randint(000000,999999))
            if num not in e:
                return str(num)

    def encrypt_password(self, input_password):
        all_punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        result = ""
        start = "^^^"
        end = "$$$"
        a = 1
        # decide the type and quantity of punctuation to use in encryption
        first = all_punctuation[len(input_password) % len(all_punctuation)]
        second = all_punctuation[len(input_password) % 5]
        third = all_punctuation[len(input_password) % 10]
        result += start
        # insert punctuation into the password and loop
        for index in input_password:
            if a % 3 == 1:
                result += (first + index + first)
            elif a % 3 == 2:
                result += (second * 2 + index + second * 2)
            elif a % 3 == 0:
                result += (third * 3 + index + third * 3)
            a += 1
        result += end
        return result

    def register_user(self, username, password, email, register_time, role):
        if self.check_username_exist(username):
            return False
        else:
            id = self.generate_unique_user_id()
            password = self.encrypt_password(password)
            register_time = self.date_conversion(register_time)

            if role == "instructor":
                user = [id, username, password, register_time, role, email, '', '', '']
            elif role == "student":
                user = [id, username, password, register_time, role, email]
            fp = open(user_data_path, 'a')
            fp.write(';;;'.join(user) + '\n')
            fp.close()
            return True

    def date_conversion(self, register_time):
        try:
            milli_second = int(str(register_time)[-3:])
            register_time = int(str(register_time)[:-3])
            # define Melbourne time zone
            register_time = register_time + (11 * 3600)
            year = 1970
            month, day, temp_year_day, month_day, hour = 0, 0, 0, 0, 0
            while register_time > 0:
                list_for_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                if register_time >= 3600:
                    register_time -= 3600
                else:
                    break
                hour += 1
                if hour % 24 == 0:
                    day += 1
                    temp_year_day += 1
                    month_day += 1
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    list_for_month[1] = 29
                    if temp_year_day == 366:
                        temp_year_day = 0
                        year += 1
                else:
                    if temp_year_day == 365:
                        temp_year_day = 0
                        year += 1
                if month_day == list_for_month[month]:
                    month_day = 0
                    month += 1
                    if month > 11:
                        month = 0
            month = month + 1
            month_day = month_day + 1
            hour = hour % 24
            mins, sec = divmod(register_time, 60)

            return '{}-{}-{}_{}:{}:{}.{}'.format(year, month, month_day, hour, mins, sec, milli_second)
        except:
            return 'yyyy-MM-dd  HH:mm:ss.SSS'
