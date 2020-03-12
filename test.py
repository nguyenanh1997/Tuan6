from flask import Flask, request,jsonify, make_response, render_template
from flask_wtf import CSRFProtect, FlaskForm
import requests
import form
import json
import connectdb as db
import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

@app.route('/', methods=['GET'])
def submit():
    record = db.select_data()
    fo = form.MyForm()
    para = []
    for row in record:
        para.append(row[0])
    return render_template('1.html', form=fo,data=para)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001, debug = True)
