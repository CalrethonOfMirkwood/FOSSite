from flask import Blueprint, Flask, render_template


app_michael = Blueprint('michael', __name__,
                       url_prefix='/michael',
                       template_folder='templates/michael',
                       static_folder='static' ,
                       static_url_path='assets' )

@app_michael.route('/')
def michael():
    return render_template("michaelAbout.html")




