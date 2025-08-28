from flask import Flask
from flask import request
from SqlUtils import SqlUtil

app = Flask(__name__)


@app.route('/')
def welcome():
    return {'code':200,'msg':'welcome'}

@app.route('/add',methods = ['POST'])
def add():
    name = request.form.get('name')
    star = request.form.get('star')
    time = request.form.get('time')
    url = request.form.get('url')
    score = request.form.get('score')
    db = SqlUtil('127.0.0.1',3306,'root','DDL@killer49','app')
    # 使用参数化查询防止SQL注入
    res = db.select("SELECT * FROM 猫眼电影榜 WHERE name = %s;", (name,))
    if len(res) != 0:
        return {'code':400,'msg':'movie already exist in the top100'}
    db.execute("INSERT INTO 猫眼电影榜 VALUES(%s, %s, %s, %s, %s);", (name, star, time, url, score))
    return {'code':200,'msg':'add success'}

@app.route('/delete')
def delete():
    name = request.args.get('name')
    db = SqlUtil('127.0.0.1',3306,'root','DDL@killer49','app')
    # 使用参数化查询防止SQL注入
    res = db.select("SELECT * FROM 猫眼电影榜 WHERE name = %s;", (name,))
    if len(res) == 0:
        return {'code':400,'msg':'movie not found'} 
    db.execute("DELETE FROM 猫眼电影榜 WHERE name = %s;", (name,))
    return {'code':200,'msg':'delete success'} # 统一返回格式

@app.route('/update',methods=['POST'])
def update():
    name = request.form.get('name')
    star = request.form.get('star')
    time = request.form.get('time')
    url = request.form.get('url')
    score = request.form.get('score')
    db = SqlUtil('127.0.0.1',3306,'root','DDL@killer49','app')

    res = db.select("SELECT * FROM 猫眼电影榜 WHERE name = %s;", (name,))
    if len(res) == 0:
        return {'code':400,'msg':'更改失败'}

    db.execute("UPDATE 猫眼电影榜 SET star = %s, time = %s, url = %s, score = %s WHERE name = %s;", (star, time, url, score, name))
    return {'code':200,'msg':'更改成功'}
    
@app.route('/search')
def search():
    name = request.args.get('name')
    db = SqlUtil('127.0.0.1',3306,'root','DDL@killer49','app')
    
    # 构建模糊查询的 SQL 语句，使用参数化查询
    # 注意：对于LIKE查询，通配符需要包含在参数中，而不是SQL字符串中
    sql = "SELECT * FROM 猫眼电影榜 WHERE name LIKE %s;"
    res = db.select(sql, (f'%{name}%',)) # 将通配符作为参数的一部分
    
    if len(res) == 0:
        return {'code':404,'msg':'未找到相关电影'}
    else:
        movies = []
        for row in res:
            movie_info = {
                'name': row[0],
                'star': row[1],
                'time': row[2],
                'url': row[3],
                'score': row[4]
            }
            movies.append(movie_info)
        return {'code':200,'msg':'查询成功','data':movies}

if __name__ == '__main__':
    app.run(port=5005)