from flask import Flask, request
import json
import pdb
from util import JSONEncoder

from pymongo import MongoClient

app = Flask(__name__)

mongo = MongoClient('localhost', 27017)

app.db = mongo.test

@app.route('/users')
def get_users():

    name = request.args.get('name')

    users_collection = app.db.users

    result = users_collection.find_one(
        {'name': name}
    )

    response_json = JSONEncoder().encode(result)

    return (response_json, 200, None)

if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run["debug"] = True
