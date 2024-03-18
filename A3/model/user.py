import re
import random

class User:
    current_login_user = None
    def __init__(self,uid=-1, username='', password='',register_time: str = 'yyyy-MM-dd_HH:mm:ss.SSS',role =''):
        self.uid = uid
        self.username = username
        self.password = password
        self.register_time = register_time
        self.role = role
        pass

    def __str__(self):
        return str(self.uid) + ";;;" + self.username + ";;;" + self.encrypt_password(self.password)+";;;"+self.register_time+";;;"+self.role
        pass

    def validate_username(self, username):
        # replace all '_' into 'i' in order to use isalpha to check whether the username only contain alphabets and underscore
        username=username.replace('_','i')
        return username.isaplpha()
        pass

    def validate_password(self, password):
        return len(password)>=8
        pass

    def validate_email(self, email):
        match=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'
        if re.search(match,email) and len(email)>=8:
            return True
        else:
            return False
        pass

    def clear_user_data(self):
        f = open('data/user.txt', 'w')
        f.close()
        pass

    def authenticate_user(self, username, password):
        user_dict={}
        with open ('data/user.txt','r') as users:
            for user in users.readlines():
               user_data=user.strip().split(';;;')
               if len(user_data) != 0:
                   user_dict[user_data[1]] = user_data
        try:
            if user_dict[username][2]==self.encrypt_password(password):
                # if the login detail is correct the return True
                return True,';;;'.join(user_dict[username])
            else:
                # if the password is incorrect the return False
                return False,''
        except KeyError:
            # if the username is incorrect the return False
            return False,''
        pass

    def check_username_exist(self, username):
        for line in open('data/user.txt').readlines():
            line = line.strip()
            sp = line.strip().split(";;;")
            username = sp[1]
            if self.username == username:
                return True
        return False
        pass

    def generate_unique_user_id(self):
        ids = set()
        for line in open('data/user.txt').readlines():
            sp = line.split(';;;')
            id = int(sp[0])
            ids.add(id)
            while True:
                random_id = random.randint(100000, 999999)
                if random_id not in ids:
                    return random_id
        pass

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
        # Perform authentication and return tuple for result, role and info
        pass

    def register_user(self, username, password, email, register_time, role):
        if self.check_username_exist(username):
            return False
        else:
            id = self.generate_unique_user_id()
            password = self.encrypt_password(password)
            register_time = self.date_conversion(register_time)

            if role == 'Admin':
                user = [id, username, password, register_time, role]
            elif role == "Instructor":
                user = [id, username, password, register_time, role, email, '', '', '']
            elif role == "Student":
                user = [id,username, password, register_time, role, email]
            else:
                return 'Role is incorrect'
            fp = open('data/user.txt', 'a')
            fp.write(';;;'.join(user)+'\n')
            fp.close()
            return True
        pass

    def date_conversion (self, register_time):
        milli_second = int(str(register_time)[-3:])
        register_time = int(str(register_time)[:-3])
        # define Melbourne time zone
        register_time = register_time+(11*3600)
        year = 1970
        month,day,temp_year_day,month_day,hour = 0,0,0,0,0
        while register_time > 0:
            list_for_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if register_time>=3600:
                register_time-=3600
            else:
                break
            hour += 1
            if hour % 24 == 0:
                day += 1
                temp_year_day += 1
                month_day+=1
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
                month_day =0
                month += 1
                if month > 11:
                    month = 0
        month = month + 1
        month_day = month_day + 1
        hour = hour % 24
        mins, sec= divmod(register_time, 60)

        return '{}-{}-{}_{}:{}:{}.{}'.format(year,month,month_day,hour,mins,sec,milli_second)

        pass

if __name__ == '__main__':
    u=User
f= open('data/_demo_user.txt')
fr=f.read()
print(fr)

