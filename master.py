# import "packages" from flask
from flask import render_template
from __init__ import app

#Pulls data for blueprints

#About Pages
from abt_pages.sophie.sophie import app_sophie
from abt_pages.krish.krish import app_krish

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


app.register_blueprint(app_sophie)
app.register_blueprint(app_krish)

# runs the application on the development server
if __name__ == "__master__":
    app.run()


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


@app.errorhandler(404)
def server_error(e):
    return render_template('404.html'), 404
