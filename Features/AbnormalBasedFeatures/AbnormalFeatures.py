# -1 ----> Phishing
# 0  ----> Suspicious
# 1  ----> Legitimate


class AbnormalFeatures:
    def __init__(self, url):
        self.url = url

    def requestURL(self, url):
        return self.url

    def urlOfAnchor(self, url):
        return self.url

    def linksInTags(self, url):
        return self.url

    def serverFormHandler(self, url):
        return self.url

    def submitMailInformation(self, url):
        return self.url

    def abnormalURL(self, url):
        return self.url
