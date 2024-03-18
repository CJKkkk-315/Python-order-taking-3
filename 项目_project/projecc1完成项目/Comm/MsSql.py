import pymssql
import pymysql

class MSSQL():
    def __init__(self, server, user, pwd, db):
        self.server = server
        self.user = user
        self.pwd = pwd
        self.db = db
        self.conn = None
        self.InitConnect()

    def __del__(self):  # 析构方法
        if self.conn:
            self.conn.close()
            print('数据库连接已关闭!')

    # '''初始链接'''
    def InitConnect(self):
        if not self.db:
            raise NameError('没有设置数据!')
        try:
            self.conn = pymssql.connect(server = self.server, user = self.user,
                                        password = self.pwd, database = self.db,
                                        charset = 'utf8')
        except Exception as msg:
            raise NameError(msg)
        else:
            self.cur = self.conn.cursor()
            if not self.cur:
                raise NameError('获取游标对象失败!')

    # '''创建连接数据库'''
    def __GetConnect(self):
        if not self.db:
            raise NameError('没有设置数据!')
        try:
            self.conn = pymssql.connect(server = self.server, user = self.user,
                                        password = self.pwd, database = self.db,
                                        charset = 'utf8')
        except Exception as msg:
            raise NameError(msg)
        else:
            cur = self.conn.cursor()
            if not cur:
                raise NameError('获取游标对象失败!')
            else:
                return cur

    # '''查询多条记录'''
    def ExeceQuery(self, strSql, *args, **kwargs):
        if self.conn is None:
            self.InitConnect()
        try:
            self.cur.execute(strSql, *args, **kwargs)
            reslist = self.cur.fetchall()
            return reslist
        except Exception as msg1:
            raise NameError(msg1)
        # try:
        #     cur = self.__GetConnect()
        # except Exception as msg:
        #     raise NameError(msg)
        # try:
        #     cur.execute(strSql, *args, **kwargs)
        #     reslist = cur.fetchall()
        #     return reslist
        # except Exception as msg1:
        #     raise NameError(msg1)
        # finally:
        #     self.conn.close()


    # '''执行sql语句'''
    def ExecNonQuery(self, strSql, *args, **kwargs):
        if self.conn is None:
            self.InitConnect()
        try:
            self.cur.execute(strSql, *args, **kwargs)
            recount = self.cur.rowcount
            self.conn.commit()
            return recount
        except Exception as msg1:
            raise NameError(msg1)
        # try:
        #     cur = self.__GetConnect()
        # except Exception as msg:
        #     raise NameError(msg)
        # try:
        #     cur.execute(strSql, *args, **kwargs)
        #     recount = cur.rowcount
        #     self.conn.commit()
        #     return recount
        # except Exception as msg1:
        #     raise NameError(msg1)
        # finally:
        #     self.conn.close()

    # '''执行sql语句'''
    def ExceSql(self, strSql, *args, **kwargs):
        if self.conn is None:
            self.InitConnect()
        try:
            self.cur.execute(strSql, *args, **kwargs)
            recount = self.cur.rowcount
            self.conn.commit()
            return recount
        except Exception as msg1:
            raise NameError(msg1)

    # '''批量导入'''
    def ExecMany(self, strSql, dtlst):
        '''
        批量插入数据使用
        :param strSql: sql 语句
        :param dtlst: 批量数据列表，每一条数据是元组
        :return:
        '''
        if not isinstance(strSql, str):
            raise TypeError
        if strSql == '':
            raise ValueError('SQL语句为空!')
        if len(dtlst) <= 0:
            raise ValueError('批量数据为空!')
        if self.conn is None:  # 如果数据库没有连接，先连接数据库
            self.InitConnect()
        try:
            self.cur.executemany(strSql, dtlst)
            self.conn.commit()
            pass
        except Exception as msg1:
            raise NameError(msg1)

class MYSQL():
    def __init__(self, server, user, pwd, db):
        self.server = server
        self.user = user
        self.pwd = pwd
        self.db = db
        self.conn = None
        self.cur = None
        self.InitConnect()

    def __del__(self):  # 析构方法
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
            print('数据库连接已关闭!')

    # '''初始链接'''
    def InitConnect(self):
        if not self.db:
            raise NameError('没有设置数据!')
        try:
            self.conn = pymysql.connect(host = self.server, user = self.user,
                                        password = self.pwd, database = self.db,
                                        charset = 'utf8', port=3306)
        except Exception as msg:
            raise NameError(msg)
        else:
            self.cur = self.conn.cursor()
            if not self.cur:
                raise NameError('获取游标对象失败!')

    # '''查询多条记录'''
    def ExeceQuery(self, strSql, *args, **kwargs):
        if self.conn is None:
            self.InitConnect()
        try:
            self.cur.execute(strSql, *args, **kwargs)
            reslist = self.cur.fetchall()
            return reslist
        except Exception as msg1:
            self.conn.rollback()
            raise NameError(msg1)


    # '''执行sql语句'''
    def ExecNonQuery(self, strSql, *args, **kwargs):
        if self.conn is None:
            self.InitConnect()
        try:
            self.cur.execute(strSql, *args, **kwargs)
            recount = self.cur.rowcount
            self.conn.commit()
            return recount
        except Exception as msg1:
            # self.conn.rollback()
            print(msg1)
            raise NameError(msg1)

    # '''批量导入'''
    def ExecMany(self, strSql, dtlst):
        '''
        批量插入数据使用
        :param strSql: 插入的sql语句，insert into table (col1,col2) values (%s,%s)
        :param dtlst: 批量数据列表，每一条数据是元组, [('aa', '11'), ('bb', '22')]
        :return:
        '''
        if not isinstance(strSql, str):
            raise TypeError
        if strSql == '':
            raise ValueError('SQL语句为空!')
        if len(dtlst) <= 0:
            raise ValueError('批量数据为空!')
        if self.conn is None:  # 如果数据库没有连接，先连接数据库
            self.InitConnect()
        try:
            self.cur.executemany(strSql, dtlst)
            self.conn.commit()
            pass
        except Exception as msg1:
            raise NameError(msg1)
