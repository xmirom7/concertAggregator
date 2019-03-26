import datetime
import urllib
import json
import sys
from bs4 import BeautifulSoup

class Songkick():
    def __init__(self):
        self.args = ''

    def GetUpcomingEventsCount(self, args):
        if self.args != args:
            self.jsonData = self.GetJsonData(args)
            self.args = args
        return len(self.jsonData)

    def GetCountryByIndex(self, index, args):
        if self.args != args:
            self.jsonData = self.GetJsonData(args)
            self.args = args
        return self.jsonData[index]['venue']['metroArea']['country']['displayName']

    def GetCityByIndex(self, index, args):
        if self.args != args:
            self.jsonData = self.GetJsonData(args)
            self.args = args
        return self.jsonData[index]['venue']['metroArea']['displayName']

    # Returned time should be in UTC.
    def GetDateByIndex(self, index, args):
        if self.args != args:
            self.jsonData = self.GetJsonData(args)
            self.args = args
        timeString = self.jsonData[index]['start']['datetime']
        if timeString == '' or timeString == None:
            timeString = self.jsonData[index]['start']['date']
            #todo timezone should be based on the country and not fixed CET
            time = datetime.datetime.strptime('{}+0100'.format(timeString), '%Y-%m-%d%z')
        else:
            time = datetime.datetime.strptime(timeString, '%Y-%m-%dT%H:%M:%S%z')
        return time

    def GetClubNameByIndex(self, index, args):
        if self.args != args:
            self.jsonData = self.GetJsonData(args)
            self.args = args
        return self.jsonData[index]['venue']['displayName']

    def GetURLByIndex(self, index, args):
        if self.args != args:
            self.jsonData = self.GetJsonData(args)
            self.args = args
        return self.jsonData[index]['uri']

    def GetInfoByIndex(self, index, args):
        if self.args != args:
            self.jsonData = self.GetJsonData(args)
            self.args = args
        return ''

    def GetJsonData(self, bandID):
        toReturn = []
        for pageNumber in range(1,99):
            url = 'https://api.songkick.com/api/3.0/artists/{}/calendar.json?apikey=GX36jP8p22qVEkTN&page={}'.format(bandID, pageNumber)
            try:
                response = urllib.request.urlopen(url).read()
            except urllib.error.HTTPError as error:
                raise Exception('Failed to get {}. {}'.format(bandID, error.read()))
            soup = BeautifulSoup(response, 'html.parser')
            data = soup.prettify()
            results = json.loads(data)['resultsPage']['results']
            if not results:
                break
            toReturn.extend(results['event'])
        return toReturn
