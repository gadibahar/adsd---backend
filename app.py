# Flask app for backend
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home(): return 'Backend Loaded'