import sqlite3
from sqlite3 import Error

class Database():
    def __init__(self, filePath):
        self.connection = sqlite3.connect(filePath)

    def GetUsedModuleNames(self):
        query = '''SELECT modules.name
        FROM bands
        INNER JOIN modules on bands.module_id = modules.id;'''
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = []
        for i in cursor.fetchall():
            result.append(i[0])
        return result

    def GetBandsModulesArgs(self):
        query = '''SELECT bands.name,modules.name,bands.module_arg
        FROM bands
        INNER JOIN modules on bands.module_id = modules.id;'''
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def SaveEvent(self, band, country, city, date, clubName='', url='', additionalInfo=''):
        try:
            query = '''INSERT INTO events(band, country, city, clubName, date, url, additionalInfo)
            VALUES(?,?,?,?,?,?,?);'''
            cursor = self.connection.cursor()
            cursor.execute(query, (band, country, city, clubName, date, url, additionalInfo))
            self.connection.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as error:
            #When the row already exists in database, just continue.
            if str(error) != 'UNIQUE constraint failed: events.band, events.country, events.city, events.clubName, events.date, events.url, events.additionalInfo':
                raise error

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()
