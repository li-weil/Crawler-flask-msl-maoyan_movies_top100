import pymysql

class SqlUtil:
    def __init__(self,_host,_port,_user,_pwd,_db):
        self.host = _host
        self.port = _port
        self.user = _user
        self.pwd = _pwd
        self.db = _db

    def getConnect(self):
        return pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.pwd,database=self.db)

    def execute(self, sql, params=None): 
        db = self.getConnect()
        cs = db.cursor()
        if params: 
            cs.execute(sql, params)
        else:
            cs.execute(sql)
        db.commit()
        cs.close()
        db.close()

    def select(self, sql, params=None) : 
        db = self.getConnect()
        cs = db.cursor()
        if params: 
            cs.execute(sql, params)
        else:
            cs.execute(sql)
        res = cs.fetchall()
        cs.close()
        db.close()
        return res


if __name__ == '__main__':

    # db = SqlUtil('127.0.0.1',3306,'root','DDL@killer49','app')
    # name = 'ddl'
    # sql = f''' drop table if exists {name}; ''' 
    # db.execute(sql)
    # sql = f''' create table {name}(id int,name varchar(20),date date); '''
    # db.execute(sql)
    # sql = f''' insert into {name} values(1,'ddl','2000-01-01'); '''
    # db.execute(sql)
    # db.execute(f''' insert into {name} values(2,'ddl','2000-01-01'); ''')
    # db.execute(f''' insert into {name} values(3,'ddl','2000-01-01'); ''')
    # sql = f''' select * from {name}; '''
    # res = db.select(sql)    
    # print(res)   
    pass