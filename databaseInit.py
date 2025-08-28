from SqlUtils import SqlUtil
import pandas as pd

def create_table():
    
    
    table_name = '猫眼电影榜'
    db.execute(f''' drop table if exists {table_name}; ''')
    sql = f'''
            create table {table_name}(
                name varchar(20) primary key comment '电影名称',
                star varchar(255) comment '主演',
                time varchar(20) comment '上映时间',
                url varchar(255) comment '电影链接',
                score varchar(20) comment '评分'
                );
            '''
    db.execute(sql)    

def data_insert():
    df = pd.read_excel('maoyan.xlsx',sheet_name='猫眼电影数据')
    for i in range(df.shape[0]):
        name = df.iloc[i,0]
        star = df.iloc[i,1]
        time = df.iloc[i,2]
        url = df.iloc[i,3]
        score = df.iloc[i,4]
        sql = '''insert into 猫眼电影榜 values(%s,%s,%s,%s,%s);'''
        db.execute(sql, (name, star, time, url, score))

if __name__ == '__main__':
    db = SqlUtil('127.0.0.1',3306,'root','DDL@killer49','app')
    create_table()
    data_insert()
