from bs4 import BeautifulSoup
import requests


def getResponse(url):
    try:
        resp = requests.get(url)
        response = resp.text
    except:
        return -1
    return response


def getSoup(response):
    try:
        soup = BeautifulSoup(response, 'html.parser')
    except:
        return -1
    return soup
