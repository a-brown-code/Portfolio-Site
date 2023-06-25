import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

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

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), experiences=experiences_lst, people=fellows_list)
