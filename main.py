
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql9288391:WuEgkaD75q@sql9.freemysqlhosting.net/sql9288391'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))  

@app.route('/')
def index():
    results = Comments.query.all()
    return render_template('index.html', results=results)

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/process',methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    entry = Comments(name=name,comment=comment)
    db.session.add(entry)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/hello', methods=['GET','POST'])
def hello():
    links = ['http://youtube.com','https://bing.com','https://yahoo.com','https://espn.com']
    return render_template('hello.html',links=links)

if __name__ == '__main__':
    app.run(debug=True)

