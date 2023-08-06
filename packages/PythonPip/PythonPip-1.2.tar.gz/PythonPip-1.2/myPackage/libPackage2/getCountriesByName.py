import requests


class getCountriesByName:
    def __init__(self, litera):
        self.litera = litera
        message = "empty"
    def getCitiesByLetter(self):
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
        querystring = {"namePrefix": self.litera}
        headers = {
            'x-rapidapi-key': "32218ce6eemsh996ede13da25217p103011jsn32357c73ded7",
            'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        countries = response.json()
        print([i['name'] for i in countries['data']])
        global message
        message = [i['name'] for i in countries['data']]
    def getNumberOfCitiesbyLetter(self):
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries"

        querystring = {"namePrefix": self.litera}

        headers = {
            'x-rapidapi-key': "32218ce6eemsh996ede13da25217p103011jsn32357c73ded7",
            'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        countries = response.text
        print(countries[-5]+countries[-4]+countries[-3])
        global message
        message = (countries[-5]+countries[-4]+countries[-3])
    def getMessage(self):
        global message
        return message