import os
from flask import Flask, render_template, request, Response
from dotenv import load_dotenv
import folium
import json
from pathlib import Path
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = None
if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), host=os.getenv("MYSQL_HOST"), port=3306)
print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

def load_work_experience():
    work_file_path = Path(__file__).resolve().parent / 'static' / 'data' / 'work.json'

    with open(work_file_path, 'r') as f:
        work_data = json.load(f)
    
    return work_data['work']

def load_fellows():
    work_file_path = Path(__file__).resolve().parent / 'static' / 'data' / 'work.json'

    with open(work_file_path, 'r') as f:
        work_data = json.load(f)
    
    return work_data['fellows']

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
    
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), map=map_html, members=members, members_education=members_education, experiences=load_work_experience(), people=load_fellows(), about_us=load_about_us_data())

@app.route('/hobbies')
def hobbies():
    members_hobbies = load_member_hobby_data()
    
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), members_hobbies = members_hobbies)

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    # POST request missing name
    if "name" not in request.form.keys():
        return Response("Invalid name", status=400)

    # POST request with empty content
    if request.form['content'].isspace():
        return Response("Invalid content", status=400)

    # POST request with malformed email
    if request.form['email'] == "not-an-email":
        return Response("Invalid email", status=400)

    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]
    }

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")