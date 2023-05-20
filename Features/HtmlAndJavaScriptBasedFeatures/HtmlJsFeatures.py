# -1 ----> Phishing
# 0  ----> Suspicious
# 1  ----> Legitimate
import requests


class HtmlJsFeatures:
    def __init__(self, url):
        self.url = url

    def websiteForwarding(self):
        try:
            resp = requests.get(self.url).history
            if len(resp) <= 1:
                return 1
            elif 2 <= len(resp) < 4:
                return 0
            else:
                return -1
        except:
            return -1

    def statusBarCustom(self):
        return self.url

    def disableRightClick(self):
        return self.url

    def usingPopUpWindow(self):
        return self.url

    def iFrameRedirection(self):
        return self.url
