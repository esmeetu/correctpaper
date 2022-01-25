#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import uuid
import base64
import requests

from project_29 import computation1

from flask import Flask, request
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

CORS(app, resources=r'/*')

app.config['UPLOAD_FOLDER'] = './dist/static'
app.debug = True


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        return json.dumps({'filename': f_name})


@app.route('/learn', methods=['POST'])
def learn():
    if request.method == 'POST':
        data = json.loads(str(request.data))
        type = data['type']
        image_uri = "data:image/jpg;base64," + base64.b64encode(
            open(os.path.join(app.config['UPLOAD_FOLDER'][:-6], data['sourceUrl']), "rb").read())
        try:
            r = requests.post("https://api.mathpix.com/v3/latex",
                              data=json.dumps({'src': image_uri}),
                              headers={"app_id": '',
                                       "app_key": '',
                                       "Content-type": "application/json"})
            r.raise_for_status()
        except requests.RequestException as e:
            return json.dumps({'answer': "image recognition fail"})
        except TypeError:
            print("TypeError:请重写答案!")
        except ValueError:
            print("ValueError:请重写答案!")
        except IOError:
            print("IOErrors:请重写答案!")
        else:
            re_rate = json.loads(r.text)['latex_confidence']
            put = json.loads(r.text)['latex']
            return computation1.out_print(re_rate, int(type['value']), put)


if __name__ == '__main__':
    app.run()
