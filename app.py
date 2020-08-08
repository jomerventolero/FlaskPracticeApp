'''
    Documentation v1.0.0

    Author: Jomer Ventolero
    Email: orekihoutaro1218@gmail.com
    Company: Adarna Reborn Game Dev

'''

from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template("homepage.html")

@app.route('/about')
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.run(debug=True)
