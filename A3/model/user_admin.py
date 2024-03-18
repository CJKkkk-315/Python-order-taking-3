from user import User
class Admin(User):
    def __init__(self,uid=-1, username='', password=''):
        self.uid = uid
        self.username = username
        self.password = password
        pass

    def register_admin(self):
        # read every line in the user_admin.txt adn check whether the username exist already or not
        for line in open('data/user.txt').readlines():
            sp = line.strip().split(";;;")
            uid = int(sp[0])
            name = sp[1]
            password = sp[2]
            # if the username does not exist the write it into the user_admin.txt
            # if exist then do nothing
            if self.uid == uid and self.username == name and self.encrypt_password(self.password) == password:
                return
        fp = open('data/user.txt', 'a')
        fp.write(self.__str__() + '\n')
        fp.close()
        pass

    def __str__(self):
        return '{};;;{};;;{};;;{}'.format(self.uid,self.username,self.encrypt_password(self.password))
        pass