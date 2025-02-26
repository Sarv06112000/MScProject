# -1 ----> Phishing
# 0  ----> Suspicious
# 1  ----> Legitimate

from Features import Patterns as Pattern
import requests
import re
from bs4 import BeautifulSoup
import networkx as nx
import socket


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
        try:
            response = requests.get(f"https://www.google.com/search?q=site:{self.url}")
            if response.text.find("did not match any documents") == -1:
                return 1
            else:
                return -1
        except:
            return -1

    def linkPointingPage(self, soup):
        try:
            anchors = soup.find_all("a", href=True)
            if len(anchors) == 0:
                return -1
            elif 0 < len(anchors) >= 2:
                return 0
            else:
                return 1
        except:
            return -1

    def statisticReport(self):
        try:
            url_match = re.search(
                'at\.ua|usa\.cc|baltazarpresentes\.com\.br|pe\.hu|esy\.es|hol\.es|sweddy\.com|myjino\.ru|96\.lt|ow\.ly',
                self.url)
            ip_address = socket.gethostbyname(self.url)
            ip_match = re.search(
                '146\.112\.61\.108|213\.174\.157\.151|121\.50\.168\.88|192\.185\.217\.116|78\.46\.211\.158|181\.174\.165\.13|46\.242\.145\.103|121\.50\.168\.40|83\.125\.22\.219|46\.242\.145\.98|'
                '107\.151\.148\.44|107\.151\.148\.107|64\.70\.19\.203|199\.184\.144\.27|107\.151\.148\.108|107\.151\.148\.109|119\.28\.52\.61|54\.83\.43\.69|52\.69\.166\.231|216\.58\.192\.225|'
                '118\.184\.25\.86|67\.208\.74\.71|23\.253\.126\.58|104\.239\.157\.210|175\.126\.123\.219|141\.8\.224\.221|10\.10\.10\.10|43\.229\.108\.32|103\.232\.215\.140|69\.172\.201\.153|'
                '216\.218\.185\.162|54\.225\.104\.146|103\.243\.24\.98|199\.59\.243\.120|31\.170\.160\.61|213\.19\.128\.77|62\.113\.226\.131|208\.100\.26\.234|195\.16\.127\.102|195\.16\.127\.157|'
                '34\.196\.13\.28|103\.224\.212\.222|172\.217\.4\.225|54\.72\.9\.51|192\.64\.147\.141|198\.200\.56\.183|23\.253\.164\.103|52\.48\.191\.26|52\.214\.197\.72|87\.98\.255\.18|209\.99\.17\.27|'
                '216\.38\.62\.18|104\.130\.124\.96|47\.89\.58\.141|78\.46\.211\.158|54\.86\.225\.156|54\.82\.156\.19|37\.157\.192\.102|204\.11\.56\.48|110\.34\.231\.42',
                ip_address)
            if url_match:
                return -1
            elif ip_match:
                return -1
            return 1
        except:
            return 1
