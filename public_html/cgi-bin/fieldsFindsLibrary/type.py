#!/usr/bin/env python3
__all__ = ['Type']

"""
This class creates the blueprint for the dropdown menu from which type can be
selected finds can be filtered.
"""

class Type(object):
    # Use __init__ to assign the values belonging to that class;
    # in which self refers to the class instance itself, and is referred to
    # across the variables that belong to the type class

    def __init__(self, typeId, name, period, use):
        self.typeId = str(typeId)
        self.name = str(name)
        self.period = str(period)
        self.use = str(use)

    def renderOption(self, selected_type):
        typeOption = '<option '
        typeOption = typeOption + 'value="' + str(self.typeId) + '"'

        # If statement which causes the selected type to remain selected when the
        # page is reloaded
        if int(selected_type or 0) == int(self.typeId):
            typeOption = typeOption + ' selected="selected"'
        typeOption = typeOption + '>'
        typeOption = typeOption + str(self.name)
        typeOption = typeOption + '</option>'

        return typeOption
