import urllib
import json
import sys
import datetime
from bs4 import BeautifulSoup

class Bandsintown():
    def __init__(self):
        self.bandName = ''

    def GetUpcomingEventsCount(self, bandName):
        if self.bandName != bandName:
            self.jsonData = self.GetJsonData(bandName)
            self.bandName = bandName
        return len(self.jsonData)

    def GetCountryByIndex(self, index, bandName):
        if self.bandName != bandName:
            self.jsonData = self.GetJsonData(bandName)
            self.bandName = bandName
        return self.jsonData[index]['venue']['country']

    def GetCityByIndex(self, index, bandName):
        if self.bandName != bandName:
            self.jsonData = self.GetJsonData(bandName)
            self.bandName = bandName
        return self.jsonData[index]['venue']['city']

    # Returned time should be in UTC.
    def GetDateByIndex(self, index, bandName):
        if self.bandName != bandName:
            self.jsonData = self.GetJsonData(bandName)
            self.bandName = bandName
        dateString = self.jsonData[index]['datetime']
        #todo timezone should be based on the country and not fixed CET
        dtm = datetime.datetime.strptime('{}+0100'.format(dateString), '%Y-%m-%dT%H:%M:%S%z')
        return dtm

    def GetClubNameByIndex(self, index, bandName):
        if self.bandName != bandName:
            self.jsonData = self.GetJsonData(bandName)
            self.bandName = bandName
        return self.jsonData[index]['venue']['name']

    def GetURLByIndex(self, index, bandName):
        if self.bandName != bandName:
            self.jsonData = self.GetJsonData(bandName)
            self.bandName = bandName
        return self.jsonData[index]['url']

    def GetInfoByIndex(self, index, bandName):
        if self.bandName != bandName:
            self.jsonData = self.GetJsonData(bandName)
            self.bandName = bandName
        return self.jsonData[index]['description']

    def GetJsonData(self, bandName):
        encodedName = urllib.parse.quote(bandName.encode('utf-8'))
        url = 'https://rest.bandsintown.com/artists/{}/events?app_id=js_www.konflikt.sk&date=upcoming'.format(encodedName)
        response = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(response, 'html.parser')
        data = soup.prettify()
        return json.loads(data)
