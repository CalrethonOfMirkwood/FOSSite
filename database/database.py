from flask import Flask, render_template, request, Blueprint
import sqlite3 as sql
app_database = Blueprint('database', __name__,
                        url_prefix='/database',
                        template_folder='templates',
                        static_folder='static' ,
                        static_url_path='assets' )

@app_database.route('/')
def database():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    command ="""CREATE TABLE IF NOT EXISTS
    database(name TEXT, title TEXT, img TEXT, post TEXT)"""

    cur.execute(command)
    cur.execute("select * from database")

    rows = cur.fetchall();
    return render_template("database.html",rows = rows)

@app_database.route('/enternew')
def enternew():
    return render_template('enternew.html')

@app_database.route('/post',methods = ['POST', 'GET'])
def addpost():
    if request.method == 'POST':
        try:
            name = request.form['name']
            title = request.form['title']
            img = request.form['img']
            post = request.form['post']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO database (name,title,img,post) VALUES (?,?,?,?)",(name,title,img,post) )
                con.commit()
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html")
            con.close()
