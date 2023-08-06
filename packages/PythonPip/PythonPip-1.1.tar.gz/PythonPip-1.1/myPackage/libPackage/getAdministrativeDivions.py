import requests
class getAdministrativeDivisions:
    message = ""
    def getDivisionsForLetter(self):
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions"

        querystring = {"minPopulation": "20000000"}

        headers = {
            'x-rapidapi-key': "32218ce6eemsh996ede13da25217p103011jsn32357c73ded7",
            'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        city = response.json()
        print([i['name'] for i in city['data']])
        global message
        message = [i['name'] for i in city['data']]
    def getMessage(self):
        global message
        return message
