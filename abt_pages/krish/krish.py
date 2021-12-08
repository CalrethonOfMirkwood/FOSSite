from flask import Blueprint, Flask, render_template, request


app_krish = Blueprint('krish', __name__,
                          url_prefix='/krish',
                          template_folder='templates/krish',
                          static_folder='static' ,
                          static_url_path='assets' )

@app_krish.route('/')
def krish():
    return render_template("krish_abt.html")




