from flask import Flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/user/<name>')
def user(name):
    return render_template('index.html', name=name)

@app.route('/')
def index():
    print(datetime.utcnow())
    return render_template('index.html', current_time=datetime.utcnow())
