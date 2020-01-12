from app import app
from flask import request, jsonify
from flask_cors import cross_origin

from app import processor

@app.route('/process', methods = ['POST'])
@cross_origin()
def process():
    data = request.json
    return jsonify(processor.process(data))