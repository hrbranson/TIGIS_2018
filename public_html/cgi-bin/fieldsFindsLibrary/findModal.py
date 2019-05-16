#!/usr/bin/env python3
__all__ = ['FindModal']

"""
This class provides the blueprint to build the find information modal
"""

# Import the relevant modules
from jinja2 import Environment, FileSystemLoader
from .database import Database

class FindModal(object):

    # Initialise parameters
    def __init__(self, params):
        self.params = params
        self.env = Environment(loader=FileSystemLoader('.'))

    def render(self):
        # init db object (open database connection)
        db = Database()

        # get form parameters
        find_id = self.params.getvalue('findId')

        # load find from db
        find = db.loadFind(int(find_id or 1))

        # close db connection
        db.close()

        # Render template
        temp = self.env.get_template('templates/find_modal.html')
        return temp.render(Find=find)
