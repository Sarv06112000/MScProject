# -1 ----> Phishing
# 0  ----> Suspicious
# 1  ----> Legitimate


class HtmlJsFeatures:
    def __init__(self, url):
        self.url = url

    def websiteForwarding(self):
        return self.url

    def statusBarCustom(self):
        return self.url

    def disableRightClick(self):
        return self.url

    def usingPopUpWindow(self):
        return self.url

    def iFrameRedirection(self):
        return self.url
