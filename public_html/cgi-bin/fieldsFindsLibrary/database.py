#!/usr/bin/env python3
__all__ = ['Database']

"""

This class provides methods to connect and disconnect from the database, perform
the query, and loads the data for the fields, finds and type options.

"""

import cx_Oracle
from .field import Field
from .find import Find
from .type import Type

# Create constants to refer to the rows in the required table, can be updated easily if DB changes.
# Constants for the field table:
FIELD_ID=0
FIELD_LOW_X=1
FIELD_LOW_Y=2
FIELD_HI_X=3
FIELD_HI_Y=4
FIELD_AREA=5
FIELD_OWNER=6
FIELD_CROP=7
FIELD_CROP_NAME=9

# Constants for the find table:
FIND_ID = 0
FIND_XCOORD = 1
FIND_YCOORD = 2
FIND_TYPE = 3
FIND_DEPTH = 4
FIND_FIELD_NOTES = 5

# Constants for the classes table (called 'type' to avoid conflict):
TYPE_ID = 0
TYPE_NAME = 1
TYPE_PERIOD=2
TYPE_USE=3

# Class connects to the database, closes and creates a method to run the sql
# query

class Database(object):

    def __init__(self):
        # Uses the password from .txt file out of public_html folder to protect DB
        with open ("../../password.txt", 'r') as pwf:
            pw = pwf.read().strip()

        self.conn = cx_Oracle.connect(dsn="geosgen",user="s1880452",password=pw)

    # Method to close connection
    def close(self):
        self.conn.close()

    # Method to execute the SQL query
    def query(self, sql):
        c = self.conn.cursor()
        return c.execute(sql)


    def loadFields(self):
        # Execute the SQL query using defined method
        result = self.query("select fields.*, crops.* from gisteach.fields left outer join gisteach.crops on fields.crop=crops.crop")

        fields = []
        for row in result:
            # Loop around result of the SQL query using constants listed above
            field = Field(row[FIELD_ID], row[FIELD_LOW_X], row[FIELD_LOW_Y],
                          row[FIELD_HI_X], row[FIELD_HI_Y], row[FIELD_OWNER], row[FIELD_CROP],
                          row[FIELD_CROP_NAME])

            fields.append(field)

        return fields


    def loadFinds(self, type):
        # Execute the SQL query using the defined method; selecting all fields
        # from the 'finds' table
        sql = "select * from gisteach.finds"
        if int(type or 0) > 0 and int(type or 0) < 5:
            sql = sql + ' WHERE TYPE=' + str(type)
        result = self.query(sql)

        finds = []
        for row in result:
            find = Find(row[FIND_ID], row[FIND_XCOORD], row[FIND_YCOORD],
                        row[FIND_TYPE], row[FIND_DEPTH], row[FIND_FIELD_NOTES], None)

            finds.append(find)

        return finds


    def loadFind(self, id):
        # Execute the SQL query using the defined method; performing left outer join to connect CLASS and FIND table
        sql = "select finds.*, class.* from gisteach.finds left outer join gisteach.class on finds.type=class.type where FIND_ID=" + str(id)

        result = self.query(sql)

        # Plus 1 to counter for the list beginning with 0
        for row in result:
            type = Type(row[FIND_FIELD_NOTES+TYPE_ID+1], row[FIND_FIELD_NOTES+TYPE_NAME+1],
                        row[FIND_FIELD_NOTES+TYPE_PERIOD+1], row[FIND_FIELD_NOTES+TYPE_USE+1])

            find = Find(row[FIND_ID], row[FIND_XCOORD], row[FIND_YCOORD],
                        row[FIND_TYPE], row[FIND_DEPTH], row[FIND_FIELD_NOTES], type)

        return find


    def loadTypes(self):
        # Execute query using defined method; selecting all from table 'class'.
        result = self.query("select * from gisteach.class")

        types = []
        for row in result:
            type = Type(row[TYPE_ID], row[TYPE_NAME], row[TYPE_PERIOD], row[TYPE_USE])
            types.append(type)

        return types
