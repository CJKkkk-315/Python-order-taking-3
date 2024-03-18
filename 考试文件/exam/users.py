from sqlalchemy import MetaData, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# 获得sqlalchemy可操作的基类
DBase = declarative_base()

# 创建连接数据库的引擎
engine = 【创建数据库连接引擎的代码】 #注意修改root密码以对应操作机器

# 获得元数据，绑定引擎
md = MetaData(bind=engine)
# 创建和数据库的连接
conn = 【创建数据库连接的代码】
# 并得到实际操作数据库的会话对象
dbsession = 【创建和数据库的会话】

# 对应user表的ORM类
class Users(DBase):
    __table__ = Table("users", md, autoload=True)

    def __init__(self):
        self.userid = 0
        self.username = "user1"
        self.password = "123"
        self.nickname = ""
        【补充ORM类的属性初始化代码】

    # 查询所有用户
    def getAll(self):
        rows = dbsession.query(Users).all()
        return rows

    def find_by_name(self, val):
        rows = 【补充根据关键字val的内容，模糊查询数据库用户表users中用户名包含val变量中关键字的所有用户】
        return rows
