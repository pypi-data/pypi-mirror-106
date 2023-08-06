import requests
import json

def rank(playerName,token):
    statRequest = requests.get(url = "https://mcplayhd.net/api/player/" + playerName + "/?token=" + token)
    statJson = statRequest.json()
    data = statJson["data"]
    rank = data["group"]
    return rank;
