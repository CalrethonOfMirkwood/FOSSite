from flask import Blueprint, Flask, render_template, request
from .silmarillionmemes import getSilmMeme, noldolante


app_sophie = Blueprint('sophie', __name__,
                          url_prefix='/sophie',
                          template_folder='templates/sophie',
                          static_folder='static' ,
                          static_url_path='assets' )

@app_sophie.route('/')
def sophie():
    return render_template("sophie.html", SilmData=getSilmMeme(), noldolante=noldolante())




@app_sophie.route('/alt/')
def sophiealt():
    return render_template("sophiealt.html", noldolante=noldolante())

"""
@app_abt_page.route('/krish/')
def krish_abt():
    return render_template("krish_abt.html")

@app_abt_page.route('/michael/')
def michaelAbout():
    return render_template("michaelAbout.html")

@app_abt_page.route('/valerie/')
def valerie():
    return render_template("val_about_me.html")
"""