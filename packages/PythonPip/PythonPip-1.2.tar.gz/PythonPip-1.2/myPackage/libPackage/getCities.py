import requests

from myPackage.libPackage2.getCountries import getCountries
from myPackage.libPackage2.getCountriesByName import getCountriesByName


class getCities:
    message = ""
    def getCitiesPopOver(self):
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
        querystring = {"minPopulation":"20000000"}
        headers = {
            'x-rapidapi-key': "32218ce6eemsh996ede13da25217p103011jsn32357c73ded7",
            'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        city = response.json()
        print([i['city'] for i in city['data']])
        global message
        message = [i['city'] for i in city['data']]
    def getMessage(self):
        global message
        return message
def main():
    countries = getCountries()
    message=""
    countries.getCountries(message)
    print(countries.getCountries(message))
if __name__ == '__main__':
    main();