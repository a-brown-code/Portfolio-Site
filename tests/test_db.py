# test_db.py

# Create a temporary database, save some records to it, and try to retrieve them.

import unittest
from peewee import *
from playhouse.shortcuts import model_to_dict
import os
os.environ['TESTING'] = 'true'

from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

    def test_timeline_post(self):
        # Create 2 timeline posts.
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2
        # TO DO: Get timeline posts and assert that they are correct
        timelineposts = [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.asc())]
        assert first_post.name == timelineposts[0]['name']
        assert first_post.email == timelineposts[0]['email']
        assert first_post.content == timelineposts[0]['content']
        assert second_post.name == timelineposts[1]['name']
        assert second_post.email == timelineposts[1]['email']
        assert second_post.content == timelineposts[1]['content']