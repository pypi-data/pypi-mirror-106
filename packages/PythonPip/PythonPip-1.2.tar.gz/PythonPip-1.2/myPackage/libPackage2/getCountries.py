import time

import requests
class getCountries:
    message = ""
    def getCountries(self,message):
        result = ""
        for x in range(19):
            offset=x*10
            url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries"

            querystring = {"offset": offset, "limit": "10"}

            headers = {
            'x-rapidapi-key': "32218ce6eemsh996ede13da25217p103011jsn32357c73ded7",
            'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            countries = response.json()
            time.sleep(1.5)
            print([i['name'] for i in countries['data']])
            message = [i['name'] for i in countries['data']]
            result = result,message
        return result
    def getMessage(self):
        global message
        return message