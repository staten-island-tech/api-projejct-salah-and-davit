import requests
import json 
thing = requests.get('https://www.balldontlie.io/api/v1/teams/').json()
print(thing)
for list in thing:
        for team in list:
            teamname = list["id"]
            print(teamname)
            break
