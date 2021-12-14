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
