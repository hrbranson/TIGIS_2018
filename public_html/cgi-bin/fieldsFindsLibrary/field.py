#!/usr/bin/env python3
__all__ = ['Field']

"""
This class creates a blueprint for creating the Field objects on the website.
"""

class Field(object):
    # Use __init__ to assign the values belonging to that class;
    # in which self refers to the class instance itself, and is referred to
    # across the variables that belong to the field class

    def __init__(self, fieldId, lowX, lowY, highX, highY, owner, cropId, cropName):
        self.fieldId = int(fieldId)
        self.lowX = int(lowX)
        self.lowY = int(lowY)
        self.highX = int(highX)
        self.highY = int(highY)
        self.owner = str(owner)
        self.cropId = int(cropId)
        self.cropName = str(cropName)

        # This calculates the width of the field using the x coordinates.
        self.width = self.highX - self.lowX
        # This calculates the height of the field using the y coordinates.
        self.height = self.highY - self.lowY

        # Calculates the location of the field number labels
        self.ylab = self.highY - 1.3
        self.xlab = self.lowX + 0.3

        self.fieldnoy = self.ylab + 0.35
        self.fieldnox = self.xlab + 0.35

    # Method that renders the rectangles in HTML using the variables assigned in the
    # above method
    def renderRect(self):
        fieldSVG = '<rect '
        fieldSVG = fieldSVG + 'id="field' + str(self.fieldId) + '" '
        fieldSVG = fieldSVG + 'x="' + str(self.lowX) + '" '
        fieldSVG = fieldSVG + 'y="' + str(self.lowY) + '" '
        fieldSVG = fieldSVG + 'width="' + str(self.width) + '" '
        fieldSVG = fieldSVG + 'height="' + str(self.height) + '" '

        # Fill the background of the image with the picture of fields linked in HTML
        fieldSVG = fieldSVG + 'fill="url(#fieldimage)" stroke="black" stroke-width="0.05"'
        fieldSVG = fieldSVG + '>'

        # Create the title for each field, so that owner and crop name appears
        # when the cursor is on the field
        fieldSVG = fieldSVG + '<title>'
        fieldSVG = fieldSVG + 'Field: ' + str(self.fieldId) + ' ' '<br>'
        fieldSVG = fieldSVG + 'Owner: ' + self.owner + ' ' '<br>'
        fieldSVG = fieldSVG + 'Crop: ' + str(self.cropName)
        fieldSVG = fieldSVG + '</title>'
        fieldSVG = fieldSVG + '</rect>'

        fieldSVG = fieldSVG + '<rect '
        fieldSVG = fieldSVG + 'id="' + str(self.fieldId) + '" '
        fieldSVG = fieldSVG + 'x="' + str(self.xlab) + '" '
        fieldSVG = fieldSVG + 'y="' + str(self.ylab) + '" '
        fieldSVG = fieldSVG + 'width="' + str(1) + '" '
        fieldSVG = fieldSVG + 'height="' + str(1) + '" '
        fieldSVG = fieldSVG + 'fill="#c2d1f0" stroke="black" stroke-width="0.05" opacity="0.6"'
        fieldSVG = fieldSVG + '>'
        fieldSVG = fieldSVG + '</rect>'

        fieldSVG = fieldSVG + '<g transform="scale(1, -1)">'
        fieldSVG = fieldSVG + '<text '
        fieldSVG = fieldSVG + 'x="' + str(self.fieldnox) + '" '
        fieldSVG = fieldSVG + 'y="-' + str(self.fieldnoy) + '" '
        fieldSVG = fieldSVG + 'fill="black" font-size="0.5"'
        fieldSVG = fieldSVG + '>'
        fieldSVG = fieldSVG + str(self.fieldId)
        fieldSVG = fieldSVG + '</text>'
        fieldSVG = fieldSVG + '</g>'

        return fieldSVG
