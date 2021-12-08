# import "packages" from flask
from flask import render_template
from __init__ import app
from silmarillionmemes import getSilmMeme, noldolante
#Pulls data for blueprints

#About Pages

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/abt_pages/sophie')
def sophie():
    return render_template("abt_pages/sophie.html", SilmData=getSilmMeme(), noldolante=noldolante())




@app.route('/abt_pages/sophiealt')
def sophiealt():
    return render_template("abt_pages/sophiealt.html", noldolante=noldolante())


@app.route('/abt_pages/krish/')
def krish_abt():
    return render_template("abt_pages/krish_abt.html")

@app.route('/abt_pages/michael/')
def michaelAbout():
    return render_template("michaelAbout.html")

@app.route('/abt_pages/valerie/')
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
