# -1 ----> Phishing
# 0  ----> Suspicious
# 1  ----> Legitimate


class DomainFeatures:
    def __init__(self, url):
        self.url = url

    def ageOfDomain(self):
        return self.url

    def dnsRecord(self):
        return self.url

    def websiteTraffic(self):
        return self.url

    def pageRank(self):
        return self.url

    def googleIndex(self):
        return self.url

    def linkPointingPage(self):
        return self.url

    def statisticReport(self):
        return self.url
