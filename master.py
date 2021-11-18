# import "packages" from flask
from flask import Flask, render_template
from silmarillionmemes import getSilmMeme

# create a Flask instance
app = Flask(__name__)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sophie/')
def sophie():
    return render_template("sophie.html", SilmData=getSilmMeme())

# runs the application on the development server
if __name__ == "__master__":
    app.run()