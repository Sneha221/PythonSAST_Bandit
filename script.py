from flask import Flask, request, Response
from functools import wraps
import json
import os
import pickle
import jwt
import markdown
import markdown2
import random
import copy
import uuid
from datetime import datetime, timedelta
import time
import requests
from collections import ChainMap
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import numpy as np

app = Flask(__name__)

@app.route('/v1/', methods=['GET'])
def index():
    return "Resource App!"

@app.route('/v1/vuln1', methods=['GET'])
def vuln1():
    file = open('vuln1.txt', 'r')
    data = file.read()
    file.close()
    return data

@app.route('/v1/vuln2', methods=['GET'])
def vuln2():
    user = request.args.get('user')
    return 'Hello, ' + user + '!'

@app.route('/v1/vuln3', methods=['GET'])
def vuln3():
    cookie = request.cookies.get('name')
    return 'Cookie set to: ' + cookie

@app.route('/v1/vuln4', methods=['GET'])
def vuln4():
    token = request.headers.get('Authorization')
    return 'Token: ' + token

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True, host='0.0.0.0', port=5002)                                                                                    

