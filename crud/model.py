""" database dependencies to support Users db examples """
from sqlalchemy.exc import IntegrityError
from app import db

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Users(db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(255), unique=False, nullable=False)
    title = db.Column(db.String(255), unique=False, nullable=False)
    image = db.Column(db.String(255), unique=False, nullable=False)
    post = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, user, title, image, post):
        self.user = user
        self.title = title
        self.image = image
        self.post = post

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "userID": self.userID,
            "user": self.user,
            "title": self.title,
            "image": self.image,
            "post": self.post,
            "query": "by_alc"  # This is for fun, a little watermark
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, user, title="", image="", post=""):
        """only updates values with length"""
        if len(user) > 0:
            self.user = user
        if len(title) > 0:
            self.title = title
        if len(image) > 0:
            self.image = image
        if len(post) > 0:
            self.post = post
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing section"""


def model_tester():
    print("--------------------------")
    print("Seed Data for Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Users(user='Thomas Edison', title='test', image='https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/800px-Tux.svg.png', post="1111111111")
    u2 = Users(user='Nicholas Tesla', title='hello', image='https://cdn.vox-cdn.com/thumbor/Pkmq1nm3skO0-j693JTMd7RL0Zk=/0x0:2012x1341/1200x800/filters:focal(0x0:2012x1341)/cdn.vox-cdn.com/uploads/chorus_image/image/47070706/google2.0.0.jpg', post="1111112222")
    u3 = Users(user='joe', title='hola', image='https://wordtracker-swoop-uploads.s3.amazonaws.com/uploads/ckeditor/pictures/2105/content_cool_urls_2.png', post="1111sdfsdsdfs222")
    table = [u1, u2, u3]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate title, or error: {row.title}")


def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from users')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()