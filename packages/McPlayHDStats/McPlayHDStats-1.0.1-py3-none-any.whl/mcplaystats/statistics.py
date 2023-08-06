import requests
import json

def fbLeaderboard(gameMode,position,token):
    """
    Get A Leaderboard Position's Player Name and Time, returns a string with the info.
    """
    statRequest = requests.get(url = "https://mcplayhd.net/api/fastbuilder/" + gameMode + "/top/" + "/?token=" + token)
    statJson = statRequest.json()
    data = statJson["data"]
    top = data["top"]
    postion = stats[position]
    pinfo = postion["playerInfo"]
    pstat = postion["stats"]
    pname = pinfo["name"]
    lbTime = pstat["timeBest"]
    return "Name: " + pname + ", Time: " + lbTime;
def fbStatsBestTime(gameMode,playerName,token):
    """
    Get A PB of a Player For A Certain Mode
    """
    statRequest = requests.get(url = "https://mcplayhd.net/api/fastbuilder/" + gameMode + "/stats/" + playerName + "/?token=" + token)
    statJson = statRequest.json()
    data = statJson["data"]
    stats = data["stats"]
    bestTime = stats["timeBest"]
    return bestTime / 1000;
def fbStatsAvgTime(gameMode,playerName,token):
    """
    Get The Average Time of a Player For A Certain Mode
    """
    statRequest = requests.get(url = "https://mcplayhd.net/api/fastbuilder/" + gameMode + "/stats/" + playerName + "/?token=" + token)
    statJson = statRequest.json()
    data = statJson["data"]
    stats = data["stats"]
    totalTime = stats["timeTotal"]
    wins = stats["wins"]
    return (totalTime / wins) / 1000;
def fbStatsAttempts(gameMode,playerName,token):
    """
    Get The Attempts of a Player For A Certain Mode
    """
    statRequest = requests.get(url = "https://mcplayhd.net/api/fastbuilder/" + gameMode + "/stats/" + playerName + "/?token=" + token)
    statJson = statRequest.json()
    data = statJson["data"]
    stats = data["stats"]
    sconfirmed = stats["games"]
    return games;
def fbStatsVerified(gameMode,playerName,token):
    """
    See If A Player's Time Is Verfied For A Certain Mode
    """
    statRequest = requests.get(url = "https://mcplayhd.net/api/fastbuilder/" + gameMode + "/stats/" + playerName + "/?token=" + token)
    statJson = statRequest.json()
    data = statJson["data"]
    stats = data["stats"]
    confirmed = stats["confirmed"]
    return confirmed;
def fbStatsSpeedrunVerified(gameMode,playerName,token):
    """
    See If A Player's Time Is Speedrun.com Verfied For A Certain Mode
    """
    statRequest = requests.get(url = "https://mcplayhd.net/api/fastbuilder/" + gameMode + "/stats/" + playerName + "/?token=" + token)
    statJson = statRequest.json()
    data = statJson["data"]
    stats = data["stats"]
    sconfirmed = stats["speedrunConfirmed"]
    return sconfirmed;
