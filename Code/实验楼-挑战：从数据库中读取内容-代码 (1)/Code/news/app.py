#!/usr/bin/env python3
from flask import Flask,render_template,abort
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/shiyanlou'

db =SQLAlchemy(app)
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('files'))
    content = db.Column(db.Text)

    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

    def __repr__(self):
        return '<File %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name





@app.route('/')
def index():
    return render_template('index.html',data = File.query.all())


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404




@app.route('/files/<int:id>')
def file(id):
    data = File.query.get_or_404(id)
    return render_template('file.html',content = data)




if __name__ == "__main__":
    app.run()
