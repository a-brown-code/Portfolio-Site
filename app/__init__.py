import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

about_us_text = [
    {"name": "Aerin Brown",
     "text": "Aerin Brown is an incoming second-year Software Engineering student at McGill University, and attends as a Schulich Leader Scholar. She began programming at twelve years old to follow her blossoming passion in robotics, artificial intelligence, and game design. Now, she is part of the McGill Robotics team and works on inverse kinematics and pathfinding algorithms for their Mars rover project. She also is an active member of the McGill Game Development club and the McGill Artificial Intelligence Society. She has participated in two hackathons: MAISHacks, in which her team won Best Beginner Project, and McGameJam. In the future, she hopes to continue exploring various areas of Software Engineering through internships and freelance projects."
     },
    {"name": "Add Your Name Here",
     "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis fermentum orci non sapien rhoncus tincidunt. Mauris eu ligula est. Pellentesque ut mi ornare, lacinia nisi ac, varius mi. Phasellus molestie arcu ac leo tristique, vel ultrices erat commodo. Quisque rhoncus fringilla magna, interdum feugiat est auctor eu. Nulla lacinia leo non est finibus suscipit. Maecenas ut placerat neque. Pellentesque sagittis, libero ut scelerisque congue, mauris sem bibendum tortor, id fermentum risus leo ac magna. Sed et nulla non dui interdum ultrices ut in nunc. Suspendisse potenti. Curabitur quam tortor, posuere sit amet eros eget, scelerisque consectetur sapien."
     },
    {"name": "Add Your Name Here",
     "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis fermentum orci non sapien rhoncus tincidunt. Mauris eu ligula est. Pellentesque ut mi ornare, lacinia nisi ac, varius mi. Phasellus molestie arcu ac leo tristique, vel ultrices erat commodo. Quisque rhoncus fringilla magna, interdum feugiat est auctor eu. Nulla lacinia leo non est finibus suscipit. Maecenas ut placerat neque. Pellentesque sagittis, libero ut scelerisque congue, mauris sem bibendum tortor, id fermentum risus leo ac magna. Sed et nulla non dui interdum ultrices ut in nunc. Suspendisse potenti. Curabitur quam tortor, posuere sit amet eros eget, scelerisque consectetur sapien."
     },
]

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), about_us=about_us_text)
