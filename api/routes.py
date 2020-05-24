import json
from flask import Flask, request
from flask_cors import CORS

from api.schemas import schema

app = Flask(__name__)
CORS(app)


@app.route('/cases')
def cases():
    query = request.args.get('query')
    result = schema.schema.execute(query)
    d = json.dumps(result.data)
    print("json = {}".format(result.data))
    return '{}'.format(d)
