from flask import Blueprint, Flask, render_template



app_valerie = Blueprint('valerie', __name__,
                       url_prefix='/valerie',
                       template_folder='templates/valerie',
                       static_folder='static' ,
                       static_url_path='assets' )

@app_valerie.route('/')
def valerie():
    return render_template("valerie_abt.html")


