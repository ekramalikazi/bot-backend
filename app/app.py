from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

VERSION = "0.1"


@app.route('/')
def version():
    """ Root IRI returns the API version """
    return jsonify(version=VERSION)


@app.route('/api/jenkins/call', methods=['GET', 'POST'])
def jenkins():
    app.logger.info("calling Jenkins API")
    return "Calling Jenkins API!"
