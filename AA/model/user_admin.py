from .user import User
from lib.helper import course_data_path,user_data_path,course_json_files_path,figure_save_path
class Admin(User):
    def __init__(self,uid = -1,username = '',password = '',register_time = 'yyyy-MM-dd  HH:mm:ss.SSS',role = "admin",):
        User.__init__(self,uid,username,password,register_time,role,)
    def register_admin(self):
        if self.check_username_exist(self.username):
            return False
        else:
            id = self.generate_unique_user_id()
            password = self.encrypt_password(self.password)
            register_time = self.date_conversion(self.register_time)
            user = [id, self.username, password, register_time, 'admin']
            fp = open(user_data_path, 'a')
            fp.write(';;;'.join(user) + '\n')
            fp.close()
            return True

    def __str__(self):
        return f'{self.uid};;;{self.username};;;{self.password};;;{self.register_time};;;{self.role}'