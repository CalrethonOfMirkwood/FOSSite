from flask import Flask, render_template, request, Blueprint
import sqlite3 as sql
app_database = Blueprint('database', __name__,
                        url_prefix='/database',
                        template_folder='templates',
                        static_folder='static' ,
                        static_url_path='assets' )

@app_database.route('/')
def database():
    return render_template('database.html')

@app_database.route('/enternew')
def enternew():
    return render_template('enternew.html')

@app_database.route('/post',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            name = request.form['name']
            title = request.form['title']
            post = request.form['post']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO forum (name,addr,city,pin) VALUES (?,?,?,?)",(name,title,post) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html",msg = msg)
            con.close()

@app_database.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from forum")

    rows = cur.fetchall();
    return render_template("list.html",rows = rows)


# simple listing of table
def print_tester():
    print("------------")
    print("Table: users with SQLAlchemy")
    print("------------")
    result = model_read_all()
    for row in result:
        print(row)

def print_tester2():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from users')
    print(result.keys())
    for row in result:
        print(row)

if __name__ == "__database__":
    print_tester()
    print_tester2()



