#!/usr/bin/env python3
__all__ = ['FieldsFinds']

"""
This class provides the blueprint to build the SVG finds, fields and load the
the type options for the dropdown menu.
"""

# Import the relevant modules
from jinja2 import Environment, FileSystemLoader
from .database import Database

class FieldsFinds(object):

    # Initialise parameters
    def __init__(self, params):
        self.params = params
        self.env = Environment(loader=FileSystemLoader('.'))

    # return the fieldSVG using class loadFields and database query, and renderRect
    # method to create rectangles
    def buildFieldsSVG(self, db):
        fieldSVG = ''
        fields = db.loadFields()
        for field in fields:
            fieldSVG = fieldSVG + field.renderRect()

        return fieldSVG

    # Similar to above but for the finds
    def buildFindsSVG(self, db, type):
        findsSVG = ''
        finds = db.loadFinds(type)
        for find in finds:
            findsSVG = findsSVG + find.renderCircle()

        return findsSVG

    # Creates the options for the drop down menu, as well as an (all) selection
    def buildTypeOptions(self, db, selected_type):
        typeOptions = '<option value="0">All finds</option>'
        types = db.loadTypes()
        for type in types:
            typeOptions = typeOptions + type.renderOption(selected_type)

        return typeOptions

    def render(self):
        # init db object (open database connection)
        db = Database()

        # get form parameters
        selected_type = self.params.getvalue('type')

        # build web page elements
        fields = self.buildFieldsSVG(db)
        finds = self.buildFindsSVG(db, selected_type)
        types = self.buildTypeOptions(db, selected_type)

        # close db connection
        db.close()

        # Render template
        temp = self.env.get_template('templates/index.html')
        return temp.render(SVGfields=fields, SVGfinds=finds, TypeOptions=types)
