from bs4 import BeautifulSoup
import requests


def getSoup(url):
    try:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
    except:
        return "Url does not exists"
    return soup
