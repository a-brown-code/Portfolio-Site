import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import folium

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    m = folium.Map()
    m.get_root().width = '100%'
    m.get_root().height = '100%'
    iframe = m.get_root()._repr_html_()
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), iframe=iframe)
