# import "packages" from flask
from flask import Flask, render_template
from app import app

#Pulls data for blueprints
from sophie.sophie import app_sophie
from krish.krish import app_krish
from michael.michael import app_michael
from valerie.valerie import app_valerie

# register blueprints
app.register_blueprint(app_sophie)
app.register_blueprint(app_krish)
app.register_blueprint(app_michael)
app.register_blueprint(app_valerie)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/terminal')
def terminal():
    return render_template("terminal.html")

#
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def server_error(e):
    return render_template('404.html'), 404

# runs the application on the development server
if __name__ == "__master__":
    app.run()
