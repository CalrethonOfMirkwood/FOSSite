from flask import Blueprint, Flask, render_template
import requests


app_krish = Blueprint('krish', __name__,
                       url_prefix='/krish',
                       template_folder='templates/krish',
                       static_folder='static' ,
                       static_url_path='assets' )

@app_krish.route('/')
def krish():
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

    return render_template("krish_abt.html", movie_choice=movie_list)

@app_krish.route('/linux_intro')
def linux_intro():
    return render_template("linux_intro.html")

@app_krish.route('/linux_history')
def linux_history():
    return render_template("linux_history.html")

@app_krish.route('/Fquiz')
def Fquiz():
    return render_template("Fquiz.html")