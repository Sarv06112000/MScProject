# -1 ----> Phishing
# 0  ----> Suspicious
# 1  ----> Legitimate


class HtmlJsFeatures:
    def __init__(self, url):
        self.url = url

    def websiteForwarding(self, url):
        return self.url

    def statusBarCustom(self, url):
        return self.url

    def disableRightClick(self, url):
        return self.url

    def usingPopUpWindow(self, url):
        return self.url

    def iFrameRedirection(self, url):
        return self.url
