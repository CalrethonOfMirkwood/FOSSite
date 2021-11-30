# import "packages" from flask
from flask import Flask, render_template
from silmarillionmemes import getSilmMeme, noldolante

# create a Flask instance
app = Flask(__name__)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sophie/')
def sophie():
    return render_template("sophie.html", SilmData=getSilmMeme(), noldolante=noldolante())

@app.route('/sophiealt/')
def sophiealt():
    return render_template("sophiealt.html", noldolante=noldolante())

@app.route('/krish/')
def krish_abt():
    return render_template("krish_abt.html")

@app.route('/michael/')
def michaelAbout():
    return render_template("michaelAbout.html")

@app.route('/valerie/')
def valerie():
    return render_template("val_about_me.html")

# runs the application on the development server
if __name__ == "__master__":
    app.run()

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def server_error(e):
    return render_template('404.html'), 404