import requests


def createBitlink():
    r = requests.post("https://api-ssl.bitly.com/v4/shorten")
