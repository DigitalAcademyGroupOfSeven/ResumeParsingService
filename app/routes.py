from app import app
from flask import request, jsonify
from flask_cors import cross_origin
from werkzeug.utils import secure_filename

from app import processor

@app.route('/process', methods = ['POST'])
@cross_origin()
def process():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    result = processor.process(url_for('uploaded_file', filename=filename))
    merged_dict = {key: value for (key, value) in (result.items() + request.get_json())}
    return jsonify(merged_dict)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
