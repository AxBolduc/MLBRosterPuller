import requests
from bs4 import BeautifulSoup as bs
import sys

exportList = []

teamCodes = {
    "ari": "arizona-diamondbacks",
    "atl": "atlanta-braves",
    "bal": "baltimore-orioles",
    "bos": "boston-red-sox",
    "chc": "chicago-cubs",
    "chw": "chicago-white-sox",
    "cin": "cincinnati-reds",
    "cle": "cleveland-indians",
    "col": "colorado-rockies",
    "det": "detroit-tigers",
    "hou": "houston-astros",
    "kcr": "kansas-city-royals",
    "laa": "los-angeles-angels",
    "lad": "los-angeles-dodgers",
    "mia": "miami-marlins",
    "mil": "milwaukee-brewers",
    "min": "minnesota-twins",
    "nym": "new-york-mets",
    "nyy": "new-york-yankees",
    "oak": "oakland-athletics",
    "phi": "philadelphia-phillies",
    "pit": "pittsburgh-pirates",
    "sd" : "san-diego-padres",
    "sf" : "san-francisco-giants",
    "sea": "seattle-mariners",
    "stl": "st-louis-cardinals",
    "tbr": "tampa-bay-rays",
    "tex": "texas-rangers",
    "tor": "toronto-blue-jays",
    "wsh": "washington-nationals"
}

url = "https://www.lineups.com/mlb/roster/"
teamCode = sys.argv[1]

r = requests.get(url+teamCodes[teamCode])
soup = bs(r.content, features="html.parser")

players = soup.findAll("span", attrs={"class":"player-name-col-lg"})

for player in players:
    exportList+=player.contents[0].replace(" ", ",")+"\n"

with open(f"{teamCode}.txt", "w") as outFile:
        outFile.writelines(exportList)