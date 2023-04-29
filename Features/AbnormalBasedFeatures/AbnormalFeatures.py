# -1 ----> Phishing
# 0  ----> Suspicious
# 1  ----> Legitimate


class AbnormalFeatures:
    def __init__(self, url):
        self.url = url

    def requestURL(self):
        return self.url

    def urlOfAnchor(self):
        return self.url

    def linksInTags(self):
        return self.url

    def serverFormHandler(self):
        return self.url

    def submitMailInformation(self):
        return self.url

    def abnormalURL(self):
        return self.url
