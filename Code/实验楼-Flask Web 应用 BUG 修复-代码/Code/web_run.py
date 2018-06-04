# -*- coding: UTF-8 -*-

from flask import request
from flask import Flask
from flask import render_template
from ele import ele_red_packet


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def phone_number_form():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        phone_number = request.form['phone']
        if phone_number:
            get_red_packet = ele_red_packet(phone_number)
            return render_template('index.html', phone_number=get_red_packet)
        else:
            return render_template('index.html', phone_number='手机号不能为空')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

