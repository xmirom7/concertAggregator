import sqlite3
import datetime
from sqlite3 import Error
from pathlib import Path

class Database():
    def __init__(self):
        databaseFile = '../data.sqlite3'
        path = Path(databaseFile)
        if not path.is_file():
            self.connection = sqlite3.connect(databaseFile)
            self.RunScript('structure.sql')
            self.RunScript('dataInit.sql')
        else:
            self.connection = sqlite3.connect(databaseFile)

    def RunScript(self, fileName):
        cursor = self.connection.cursor()
        with open(fileName, mode='r', encoding='utf-8') as sqlFile:
            sqlScript = sqlFile.read()
            # print(unicode(sqlScript).encode('utf-8'))
            cursor.executescript(sqlScript)
            
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
            dateString = date.astimezone(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
            query = '''INSERT INTO events(band, country, city, clubName, date, url, additionalInfo)
            VALUES(?,?,?,?,?,?,?);'''
            cursor = self.connection.cursor()
            cursor.execute(query, (band, country, city, clubName, dateString, url, additionalInfo))
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
