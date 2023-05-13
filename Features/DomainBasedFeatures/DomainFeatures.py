# -1 ----> Phishing
# 0  ----> Suspicious
# 1  ----> Legitimate

from Features import Patterns as Pattern
import requests
import re
from bs4 import BeautifulSoup
import networkx as nx


class DomainFeatures:
    def __init__(self, url):
        self.url = url

    def ageOfDomain(self, domain_info):
        try:
            create_date = domain_info.get('creation_date')[0]
            expire_date = domain_info.get('expiration_date')[0]
            domain_age = (expire_date - create_date)
        except:
            return -1
        if domain_age.days >= 366 / 2:
            return 1
        else:
            return -1

    def dnsRecord(self, domain_info):
        try:
            if len(domain_info.get("domain_name")) == 0:
                return -1
            else:
                return 1
        except:
            return -1

    def websiteTraffic(self):
        domain_name = re.findall(Pattern.DOMAIN, self.url)[0]
        try:
            resp = requests.get("https://www.semrush.com/website/"+domain_name+"/overview/")
            soup = BeautifulSoup(resp.text, 'html.parser')
            traffic = float(soup.article.b.string.replace(",", ""))
            if traffic < 100000:
                return 1
            elif traffic > 100000:
                return 0
            else:
                return -1
        except:
            return -1

    def pageRank(self, soup):
        try:
            links = []
            anchors = soup.find_all('a', href=True)
            for anchor in anchors:
                links.append(anchor.get("href"))

            # Create a directed graph representing the website structure
            graph = nx.DiGraph()
            for link in links:
                graph.add_edges_from([(link, self.url)])

            # Calculate the PageRank
            rank = nx.pagerank(graph).get(str(self.url))
            print(rank)
            if rank < 0.2:
                return -1
            else:
                return 1
        except:
            return -1

    def googleIndex(self):
        return self.url

    def linkPointingPage(self):
        return self.url

    def statisticReport(self):
        return self.url
