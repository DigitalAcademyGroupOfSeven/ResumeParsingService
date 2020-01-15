import os
from app import app
from flask import request, jsonify, url_for
from flask_cors import cross_origin
from werkzeug.utils import secure_filename

from app import processor

@app.route('/process', methods = ['POST'])
@cross_origin()
def process():
    file = request.files['fileKey']
    filename = secure_filename(file.filename)
    filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filePath)
    result = processor.process(filePath)
    print('result:', result)
    return result

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
