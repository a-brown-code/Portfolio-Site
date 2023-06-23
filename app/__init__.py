import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import folium
import json

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    # Create a map object
    m = folium.Map(min_zoom=2)

    # Get JSON data path
    locations_file_path = os.path.join(os.path.dirname(__file__), 'static', 'data', 'locations.json')

    # Load member locations from JSON file)
    with open(locations_file_path, 'r') as f:
        data = json.load(f)
        members = data['members']
        for member in members:
            color = member['color']
            locations = member['locations']
            for location in locations:
                lat = location['lat']
                lon = location['lon']
                location_name = location['name']
                location_description = location['description']
                popup_html = f'<style>h3 {{font-family: "Roboto", serif; text-align: center;}} p {{font-family: "Roboto", serif; text-align: center;}}</style> <h3>{location_name}</h3><p>{location_description}</p>'
                iframe = folium.IFrame(html=popup_html, width=250, height=100)
                marker = folium.Marker(location=[lat, lon], icon=folium.Icon(color=color, icon='star'), popup=folium.Popup(iframe), tooltip=location_name)
                marker.add_to(m)
    
    # Set map properties
    m.get_root().width = '100%'
    m.get_root().height = '100%'
    
    # Generate the HTML embed code
    map = m.get_root()._repr_html_()

    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), map=map, members=members)
