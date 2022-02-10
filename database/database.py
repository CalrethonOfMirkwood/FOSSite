from flask import render_template, Blueprint, request
from flask_restful import Api, Resource
import sqlite3

app_database = Blueprint('database', __name__, url_prefix='/FOSSchan', template_folder='templates')

api = Api(app_database)

@app_database.route('/FOSSchan2')
def crud_api():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crud_async.html", table=users_all())

class UsersAPI:
    # class for create/post
    class _Create(Resource):
        def post(self, user, title, image, post):
            po = Users(user, title, image, post)
            person = po.create()
            if person:
                return person.read()
            return {'message': f'Processed {user}, either a format error or {title} is duplicate'}, 210

    # class for read/get
    class _Read(Resource):
        def get(self):
            return users_all()

    # class for delete
    class _ReadID(Resource):
        def get(self, userid):
            po = user_by_id(userid)
            if po is None:
                return {'message': f"{userid} is not found"}, 210
            data = po.read()
            return data

    # class for read/get
    class _ReadILike(Resource):
        def get(self, term):
            return users_ilike(term)

    # class for update/put
    class _Update(Resource):
        def put(self, title, user):
            po = user_by_title(title)
            if po is None:
                return {'message': f"{title} is not found"}, 210
            po.update(user)
            return po.read()

        # class for update/put

    class _UpdateName(Resource):
        def put(self, userid, user):
            po = user_by_id(userid)
            if po is not None:
                po.update(user)
            return po.read()

    class _UpdateAll(Resource):
        def put(self, title, user, image, post):
            po = user_by_title(title)
            if po is None:
                return {'message': f"{title} is not found"}, 210
            po.update(user, image, post)
            return po.read()

    # class for delete
    class _Delete(Resource):
        def delete(self, userid):
            po = user_by_id(userid)
            if po is None:
                return {'message': f"{userid} is not found"}, 210
            data = po.read()
            po.delete()
            return data

    # building RESTapi resource
    # building RESTapi resource
    api.add_resource(_Create, '/create/<string:user>/<string:title>/<string:image>/<string:post>')
    api.add_resource(_Read, '/read/')
    api.add_resource(_ReadID, '/read/<int:userid>')
    api.add_resource(_ReadILike, '/read/ilike/<string:term>')
    api.add_resource(_Update, '/update/<string:title>/<string:user>')
    api.add_resource(_UpdateName, '/update/<int:userid>/<string:user>')
    api.add_resource(_UpdateAll, '/update/<string:title>/<string:user>/<string:image>/<string:post>')
    api.add_resource(_Delete, '/delete/<int:userid>')

@app_database.route('/')
def database():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    command ="""CREATE TABLE IF NOT EXISTS
    database(name TEXT, title TEXT, img TEXT, post TEXT, timestmp TEXT)"""

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
            timestmp = request.form['timestmp']

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO database (name,title,img,post,timestmp) VALUES (?,?,?,?)",(name,title,img,post,timestmp) )
                con.commit()
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html")
            con.close()
