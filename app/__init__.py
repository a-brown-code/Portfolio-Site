import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import json
from pathlib import Path

load_dotenv()
app = Flask(__name__)

def load_member_education_data():
    education_file_path = Path(__file__).resolve().parent / 'static' / 'data' / 'education.json'

    with open(education_file_path, 'r') as f:
        members_education_data = json.load(f)

    return members_education_data['members']

@app.route('/')
def index():
    members_education = load_member_education_data()

    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), members_education=members_education)
