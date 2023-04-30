# -1 ----> Phishing
# 0  ----> Suspicious
# 1  ----> Legitimate

import Features.Patterns as Pattern
import re
import ipaddress as ip
# import whois
import socket
import ssl
from urllib.parse import urlparse
# from Features import WebCrawling as wc


class AddressFeatures:
    def __init__(self, url):
        self.url = url

    def usingIPAddress(self):
        domain_name = re.findall(Pattern.DOMAIN, self.url)[0]
        if len(domain_name) > 0:
            try:
                if ip.ip_address(domain_name):
                    return -1
            except:
                return 1

    def longURL(self):
        if len(self.url) < 54:
            return 1
        if 54 <= len(self.url) <= 75:
            return 0
        else:
            return -1

    def tinyURL(self):
        if len(re.findall(Pattern.DOMAIN, self.url)[0]) < 12:
            return -1
        return 1

    def atRateSymbol(self):
        if re.findall('@', self.url):
            return -1
        return 1

    def redirectDoubleSlash(self):
        if self.url.rfind('//') > 6:
            return -1
        return 1

    def prefixSuffixDomain(self):
        if len(re.findall('-', re.findall(Pattern.DOMAIN, self.url)[0])) > 0:
            return -1
        return 1

    def subMultiDomain(self):
        domain_name = re.findall(Pattern.DOMAIN, self.url)[0]
        if len(re.findall('\.', domain_name)) > 2:
            return -1
        if 1 < len(re.findall('\.', domain_name)) <= 2:
            return 0
        return 1

    def httpsDomain(self, domain_info):
        domain_name = re.findall(Pattern.DOMAIN, self.url)[0]
        if 'https' in urlparse(self.url).scheme:
            try:
                ctx = ssl.create_default_context()
                with ctx.wrap_socket(socket.socket(), server_hostname=domain_name) as s:
                    s.connect((domain_name, 443))
                    cert = s.getpeercert()
            except:
                return -1
            issuer = dict(x[0] for x in cert['issuer'])
            issued_by = issuer.get('organizationName')
            domain_info = domain_info
            # whois.whois(self.url)
            create_date = domain_info.get('creation_date')[0]
            expire_date = domain_info.get('expiration_date')[0]
            domain_age = (expire_date - create_date)
            if domain_age.days >= 365 and issued_by in []:
                return 1
            elif issued_by not in []:
                return 0
        else:
            return -1

    def domainRegLength(self, domain):
        try:
            domain_info = domain
            # whois.whois(self.url)
            create_date = domain_info.get('creation_date')[0]
            expire_date = domain_info.get('expiration_date')[0]
            domain_age = (expire_date - create_date)
        except:
            return -1
        if domain_age.days <= 365:
            return -1
        else:
            return 1

    def faviconExternalDomain(self, beautifulSoup):
        domain_name = re.findall(Pattern.DOMAIN, self.url)[0]
        # soup = beautifulSoup
        # wc.getSoup(self.url)
        try:
            heads = beautifulSoup.find_all('head')
            for head in heads:
                links = head.find_all_next('link', href=True)
                for link in links:
                    if domain_name in link['href']:
                        return 1
        except:
            -1
        return -1

    def nonStandardPort(self):
        return self.url

    def httpsInDomainPart(self):
        domain_name = re.findall(Pattern.DOMAIN, self.url)[0]
        for domain in domain_name:
            if re.match('https', domain):
                return -1
            else:
                return 1


# url = "http://www.hud.ac.uk/students/"
# url = "http://www.Confirme-paypal.com/"
# url = "http://www.legitimate.com//http://www.phishing.com"
# url = "http://bit.ly/19DXSk4"
# url = "http://portal.hud.ac.uk/"
# url = "http://federmacedoadv.com.br/3f/aze/ab51e2e319e51502f416dbe46b773a5e/?cmd=_home&amp;dispatch=11004d58f5b74f8dc1e7c2e8dd4105e811004d58f5b74f8dc1e7c2e8dd4105e8@phishing.website.html"
# url = "http://127.0.0.1/fake.html"
# url = "http://0x58.0xCC.0xCA.0x62/2/paypal.ca/index.html"


# address = AddressFeatures(url)
# print(address.tinyURL())
# print(address.longURL())
# print(address.atRateSymbol())
# print(address.usingIPAddress())
# print(address.redirectDoubleSlash())
# print(address.prefixSuffixDomain())
# print(address.subMultiDomain())
# print(address.httpsDomain())
# print(address.domainRegLength())
# print(address.faviconExternalDomain())
# print(address.nonStandardPort())
# print(address.httpsInDomainPart())

