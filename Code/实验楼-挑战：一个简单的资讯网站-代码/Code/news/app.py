#!/usr/bin/env python3
from flask import Flask,render_template,abort
import os
import json
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

def filenames():
   filelist=[file.split('.')[0] for file in os.listdir('../files')]
   return filelist



@app.route('/')
def index():
    filelist = filenames()
    return render_template('index.html', filelist=filelist)

def jsonloads(filename):
    filepath = '../files/'+ filename +'.json'
    with open(filepath) as f:
        data = f.read()
    content = json.loads(data)
    return content

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404




@app.route('/files/<filename>')
def file(filename):
    filelist = filenames()
    if filename in filelist:
        content = jsonloads(filename)
        return render_template('file.html',content=content)
    else:
        abort(404)



if __name__ == "__main__":
    app.run()
