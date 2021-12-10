# import "packages" from flask
from flask import Flask, render_template
import requests
from silmarillionmemes import getSilmMeme, noldolante
import random
# create a Flask instance
app = Flask(__name__)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/abt_pages/sophie/')
def sophie():
    return render_template("abt_pages/sophie.html", SilmData=getSilmMeme(), noldolante=noldolante())

@app.route('/abt_pages/sophiealt/')
def sophiealt():
    return render_template("abt_pages/sophiealt.html", noldolante=noldolante())

@app.route('/abt_pages/krish/')
def krish_abt():
    # Link to public API, gets movie data by genre
    url = ("https://data-imdb1.p.rapidapi.com/movie/byGen/Action/")

    querystring = {"page_size":"50"}

    headers = {
        'x-rapidapi-host': "data-imdb1.p.rapidapi.com",
        'x-rapidapi-key': "b399060d5cmshdde5a342e03dbfap1a4d84jsn99009368a5f2"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    # Pulls results form data to then be sorted
    movie_list = []
    results = response.json().get('results')
    # determines if there is a value within the list
    for movie in results:
        test = movie["title"]
        movie_list.append(test)

    return render_template("abt_pages/krish_abt.html", movie_choice=movie_list)


@app.route('/abt_pages/michael/')
def michaelAbout():
    return render_template("abt_pages/michaelAbout.html")

@app.route('/abt_pages/valerie/')
def valerie():
    return render_template("abt_pages/val_about_me.html")

# runs the application on the development server
if __name__ == "__master__":
    app.run()

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def server_error(e):
    return render_template('404.html'), 404
