#!/usr/bin/env python3
__all__ = ['Find']

"""
This class creates the blueprint for the find objects on the SVG field map,
introducing four different colours for the types of find.
"""

# Create a constant for the colours of each type of find
FIND_COLOUR = ['#007bff','#28a745','#dc3545','#ffc107']

class Find(object):
    # Use __init__ to assign the values belonging to that class;
    # in which self refers to the class instance itself, and is referred to
    # across the variables that belong to the field class

    def __init__(self, findId, xcoord, ycoord, type, depth, fieldNotes, type_object):
        self.findId = int(findId)
        self.xcoord = int(xcoord)
        self.ycoord = int(ycoord)
        self.type = int(type)
        self.depth = float(depth)
        self.fieldNotes = str(fieldNotes)
        self.type_object = type_object

    # Method that renders the circles in HTML using the blueprints assigned in the
    # above method
    def renderCircle(self):
        findSVG = '<a class="show-find" xlink:href="#" data-id="' + str(self.findId) + '">'
        findSVG = findSVG + '<circle '
        findSVG = findSVG + 'id="find' + str(self.findId) + '" '
        findSVG = findSVG + 'cx="' + str(self.xcoord) + '" '
        findSVG = findSVG + 'cy="' + str(self.ycoord) + '" '
        findSVG = findSVG + 'fill="' + FIND_COLOUR[self.type-1] + '" '
        findSVG = findSVG + 'r="0.2" '
        findSVG = findSVG + '>'
        findSVG = findSVG + '<title>'
        findSVG = findSVG + 'Find: ' + str(self.findId)
        findSVG = findSVG + '</title>'
        findSVG = findSVG + '</circle>'
        findSVG = findSVG + '</a>'

        return findSVG
