# -1 ----> Phishing
# 0  ----> Suspicious
# 1  ----> Legitimate

from Features.Enums import Patterns
import re
import ipaddress as ip


class AddressFeatures:
    def __init__(self, url):
        self.url = url
        print("hello world")

    def usingIPAddress(self, url):
        domain_name = re.findall(Patterns.DOMAIN, self.url)[0]
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
        return self.url

    def atRateSymbol(self, url):
        if re.findall('@', self.url):
            return -1
        return 1

    def redirectDoubleSlash(self, url):
        if self.url.rfind('//') > 6:
            return -1
        return 1

    def prefixSuffixDomain(self, url):
        return url

    def subMultiDomain(self, url):
        return url

    def httpsDomain(self, url):
        return url

    def domainRegLength(self, url):
        return url

    def faviconExternalDomain(self, url):
        return url

    def nonStandardPort(self, url):
        return url

    def httpsInDomainPart(self, url):
        return url