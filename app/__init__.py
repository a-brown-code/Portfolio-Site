import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import json

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    # Get JSON data path
    education_file_path = os.path.join(os.path.dirname(__file__), 'static', 'data', 'education.json')

    with open(education_file_path, 'r') as f:
        members_education_data = json.load(f)

    members_education = members_education_data['members']

    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), members_education=members_education)
