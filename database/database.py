from flask import render_template, Blueprint, request
from flask_restful import Api, Resource
from database.model import Users
from app import db
import sqlite3
import random

app_database = Blueprint('database', __name__, url_prefix='/FOSSchan', template_folder='templates')

api = Api(app_database)

# SQLAlchemy extract all users from database
def users_all_alc():
    table = Users.query.all()
    json_ready = [peep.read() for peep in table]
    return json_ready

def sqlquery_2_list(rows):
    out_list = []
    keys = rows.keys()  # "Keys" are the columns of the sql query
    print(keys)
    for values in rows:  # "Values" are rows within the SQL database
        row_dictionary = {}
        count=0
        for i in keys:  # This loop lines up K, V pairs, same as JSON style
            row_dictionary[i] = values[count]
            count+=1
        row_dictionary["query"] = "by_sql"  # This is for fun a little watermark
        out_list.append(row_dictionary)  # Finally we have a out_list row
    return out_list

# Native SQL extract all users from database
def users_all_sql():
    table = db.session.execute('select * from users')
    json_ready = sqlquery_2_list(table)
    return json_ready

def users_all():
    if random.randint(0, 1) == 0:
        table = users_all_alc()
    else:
        table = users_all_sql()
    return table

    return users_all_alc()


# SQLAlchemy extract users from database matching term
def users_ilike(term):
    """filter Users table by term into JSON list (ordered by User.name)"""
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Users.query.order_by(Users.user).filter((Users.user.ilike(term)) | (Users.title.ilike(term)))
    return [peep.read() for peep in table]


# SQLAlchemy extract single user from database matching ID
def user_by_id(userid):
    """finds User in table matching userid """
    return Users.query.filter_by(userID=userid).first()


# SQLAlchemy extract single user from database matching email
def user_by_title(title):
    """finds User in table matching email """
    return Users.query.filter_by(title=title).first()


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
    con = sqlite3.connect("/database/database.db")
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
