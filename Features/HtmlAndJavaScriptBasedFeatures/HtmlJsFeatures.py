# -1 ----> Phishing
# 0  ----> Suspicious
# 1  ----> Legitimate
import requests
import re


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

    def statusBarCustom(self, resp):
        try:
            # resp = requests.get(self.url)
            if re.findall("<script>.+onmouseover.+</script>", resp):
                return -1
            else:
                return 1
        except:
            return -1

    def disableRightClick(self, resp):
        try:
            # resp = requests.get(self.url)
            if re.findall(r"event.button ?== ?2", resp):
                return -1
            else:
                return 1
        except:
            return -1

    def usingPopUpWindow(self, resp):
        try:
            # resp = requests.get(self.url)
            if len(re.findall(r"prompt\(", resp)) == 0 or len(re.findall(r"window.prompt\(", resp)) == 0:
                return -1
            else:
                return 1
        except:
            return -1

    def iFrameRedirection(self, resp):
        try:
            # resp = requests.get(self.url)
            if re.findall(r"[<iframe>|<frameBorder>]", resp):
                return -1
            else:
                return 1
        except:
            return -1
