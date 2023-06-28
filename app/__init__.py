import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import folium
import json
from pathlib import Path

load_dotenv()
app = Flask(__name__)

experiences_lst = [
    {
        "holder": "Aerin",
        "photo": "logo.svg",
        "position": "Site Reliability Engineering Fellow",
        "company": "Major League Hacking",
        "dates": "June 19 - Sept 8",
        "description": "The Site Reliability Engineering Program is an opportunity to learn how to be a great Site Reliability Engineer by completing an interactive curriculum getting you hands on experience with the tools used by thousands of companies around the world."
    }, 
    {
        "holder": "EXAMPLE",
        "photo": "avatar.jpg",
        "position": "EXAMPLE",
        "company": "EXAMPLE",
        "dates": "EXAMPLE",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam maximus volutpat rutrum. Proin nec blandit lacus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque elementum erat vitae elit hendrerit, sed ullamcorper turpis interdum. Praesent nec fringilla dolor. Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    }, 
]

fellows_list = ["Aerin", "EXAMPLE", "SAMPLE"]

def load_about_us_data():
    about_file_path = Path(__file__).resolve().parent / 'static' / 'data' / 'about.json'

    with open(about_file_path, 'r') as f:
        about_us_data = json.load(f)
    
    return about_us_data['about']

def load_member_education_data():
    education_file_path = Path(__file__).resolve().parent / 'static' / 'data' / 'education.json'

    with open(education_file_path, 'r') as f:
        members_education_data = json.load(f)

    return members_education_data['members']

def create_marker(location, color):
    marker = folium.Marker(
        location=[location['lat'], location['lon']],
        icon=folium.Icon(color=color, icon='circle-check', prefix='fa'),
        popup=folium.Popup(
            folium.IFrame(
                f'''
                <style>
                    h3 {{font-family: "Roboto", serif; text-align: center;}}
                    p {{font-family: "Roboto", serif; text-align: center;}}
                </style>
                <h3>{location['name']}</h3>
                <p>{location['description']}</p>
                ''',
                width=200,
                height=100
            )
        ),
        tooltip=location['name']
    )
    return marker


def create_map(members):
    map = folium.Map(min_zoom=2)

    for member in members:
        color = member['color']

        for location in member['locations']:
            marker = create_marker(location, color)
            marker.add_to(map)

    map.get_root().width = '100%'
    map.get_root().height = '100%'
    map_html = map.get_root()._repr_html_()
    return map_html


def load_member_locations():
    locations_file_path = Path(__file__).resolve(
    ).parent / 'static' / 'data' / 'locations.json'
    with open(locations_file_path, 'r') as f:
        data = json.load(f)
        members = data['members']
    return members

def load_member_hobby_data():
    hobby_file_path = Path(__file__).resolve().parent / 'static' / 'data' / 'hobbies.json'
    
    with open(hobby_file_path, 'r') as f:
        members_hobby_data = json.load(f)

    return members_hobby_data['members']

@app.route('/')
def index():
    members = load_member_locations()
    members_education = load_member_education_data()
    map_html = create_map(members)
    
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), map=map_html, members=members, members_education=members_education, experiences=experiences_lst, people=fellows_list, about_us=load_about_us_data())

@app.route('/hobbies')
def hobbies():
    members_hobbies = load_member_hobby_data()
    
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), members_hobbies = members_hobbies)
