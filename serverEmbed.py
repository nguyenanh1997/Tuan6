from flask import Flask, request,jsonify, make_response, render_template
from flask_wtf import CSRFProtect
import connectdb as db
import requests
import json
import os
import form
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

@app.route('/', methods=['get'])
def index():
    resp = make_response("set cookie site")
    resp.set_cookie('test','this is values test', httponly=True, secure=True)
    resp.status_code = 200
    return resp


@app.route('/blog', methods=['GET'])
def blog():
    record = db.select_data()
    fo = form.MyForm()
    page = "<html><body>"
    for row in record:
        page += "<p>" + row[0] + "</p>"
    page += '''<form method="post">
                    {{form.csrf_token}}
                </form>'''
    return render_template(page, form=fo)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5002, debug = True)
