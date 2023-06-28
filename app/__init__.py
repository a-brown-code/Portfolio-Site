import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import json
from pathlib import Path

load_dotenv()
app = Flask(__name__)

def load_about_us_data():
    about_file_path = Path(__file__).resolve().parent / 'static' / 'data' / 'about.json'

    with open(about_file_path, 'r') as f:
        about_us_data = json.load(f)
    
    return about_us_data['about']

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), about_us=load_about_us_data())
