"""control dependencies to support CRUD routes and APIs"""
from flask import Blueprint, render_template
from flask_restful import Api, Resource
import requests

from crud.sql import *

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects

app_crud_api = Blueprint('crud_api', __name__,
                         url_prefix='/crud_api',
                         template_folder='templates/crud/',
                         static_folder='static',
                         static_url_path='static')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_crud_api)


# Method #2 for CRUD
@app_crud_api.route('/')
def crud_api():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crud_async.html", table=users_all())


""" API routes section """


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


""" API testing section """


def api_tester():
    # local host URL for model
    url = 'http://localhost:5222/crud_api'

    # test conditions
    API = 0
    METHOD = 1
    tests = [
        ['/create/Wilma Flintstone/wilma@bedrock.org/123wifli/0001112222', "post"],
        ['/create/Fred Flintstone/fred@bedrock.org/123wifli/0001112222', "post"],
        ['/read/', "get"],
        ['/read/1', "get"],
        ['/read/ilike/John', "get"],
        ['/read/ilike/com', "get"],
        ['/update/wilma@bedrock.org/Wilma S Flintstone/123wsfli/0001112229', "put"],
        ['/update/wilma@bedrock.org/Wilma Slaghoople Flintstone', "put"],
        ['/delete/4', "delete"],
        ['/read/4', "get"],
        ['/delete/5', "delete"],
        ['/read/5', "get"],
        ['/update/1/Thomas Alva Edison', "put"]
    ]

    # loop through each test condition and provide feedback
    for test in tests:
        print()
        print(f"({test[METHOD]}, {url + test[API]})")
        if test[METHOD] == 'get':
            response = requests.get(url + test[API])
        elif test[METHOD] == 'post':
            response = requests.post(url + test[API])
        elif test[METHOD] == 'put':
            response = requests.put(url + test[API])
        elif test[METHOD] == 'delete':
            response = requests.delete(url + test[API])
        else:
            print("unknown RESTapi method")
            continue

        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")


def api_printer():
    print()
    print("Users table")
    for user in users_all():
        print(user)


"""validating api's requires server to be running"""
if __name__ == "__main__":
    api_tester()
    api_printer()