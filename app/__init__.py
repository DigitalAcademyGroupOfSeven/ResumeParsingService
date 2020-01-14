from flask import Flask
from flask_cors import CORS

UPLOAD_FOLDER = 'C:/resumeUpload'

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import routes