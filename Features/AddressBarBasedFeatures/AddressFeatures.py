# -1 ----> Phishing
# 0  ----> Suspicious
# 1  ----> Legitimate

import Features.Patterns as Pattern
import re
import ipaddress as ip


class AddressFeatures:
    def __init__(self, url):
        self.url = url
        print("hello world")

    def usingIPAddress(self, url):
        domain_name = re.findall(Pattern.DOMAIN, self.url)[0]
        if len(domain_name) > 0:
            try:
                if ip.ip_address(domain_name):
                    return -1
            except:
                return 1

    def longURL(self, url):
        if len(url) < 54:
            return 1
        if 54 <= len(self.url) <= 75:
            return 0
        else:
            return -1

    def tinyURL(self, url):
        if len(re.findall(Pattern.DOMAIN, self.url)[0] < 12):
            return -1
        return 1

    def atRateSymbol(self, url):
        if re.findall('@', self.url):
            return -1
        return 1

    def redirectDoubleSlash(self, url):
        if self.url.rfind('//') > 6:
            return -1
        return 1

    def prefixSuffixDomain(self, url):
        if len(re.findall('-', re.findall(Pattern.DOMAIN, self.url)[0])) > 0:
            return -1
        return 1

    def subMultiDomain(self, url):
        if len(re.findall('\.', re.findall(Pattern.DOMAIN, self.url))) > 2:
            return -1
        if 1 < len(re.findall('\.', re.findall(Pattern.DOMAIN, self.url))) <= 2:
            return 0
        return 1

    def httpsDomain(self, url):
        return self.url

    def domainRegLength(self, url):
        return self.url

    def faviconExternalDomain(self, url):
        return self.url

    def nonStandardPort(self, url):
        return self.url

    def httpsInDomainPart(self, url):
        return self.url


# url = "http://www.hud.ac.uk/students/"
# url = "http://www.Confirme-paypal.com/"
# url = "http://www.legitimate.com//http://www.phishing.com"
# url = "http://bit.ly/19DXSk4"
# url = "http://portal.hud.ac.uk/"
# url = "http://federmacedoadv.com.br/3f/aze/ab51e2e319e51502f416dbe46b773a5e/?cmd=_home&amp;dispatch=11004d58f5b74f8dc1e7c2e8dd4105e811004d58f5b74f8dc1e7c2e8dd4105e8@phishing.website.html"
# url = "http://127.0.0.1/fake.html"
# url = "http://0x58.0xCC.0xCA.0x62/2/paypal.ca/index.html"
