# -1 ----> Phishing
# 0  ----> Suspicious
# 1  ----> Legitimate
import re
import Features.Patterns as Pattern
import requests


class AbnormalFeatures:
    def __init__(self, url):
        self.url = url

    def requestURL(self, beautifulSoup):
        return beautifulSoup

    def urlOfAnchor(self, beautifulSoup):
        domain_name = re.findall(Pattern.DOMAIN, self.url)[0]
        hrefs = []
        p_count = 0
        l_count = 0
        try:
            anchorTags = beautifulSoup.find_all('a', href=True)
            for anchor in anchorTags:
                hrefs.append(anchor.get('href'))
                for h in hrefs:
                    if domain_name in h or '/' in h:
                        l_count = l_count + 1
                    else:
                        p_count = p_count + 1
            if l_count > p_count:
                return 1
            elif l_count == p_count:
                return 0
            else:
                return -1
        except:
            return -1

    def linksInTags(self, beautifulSoup):
        metas = scripts = links = []
        try:
            metaTags = beautifulSoup.find_all('meta')
            for meta in metaTags:
                metas.append(meta.get('href'))
            scriptTags = beautifulSoup.find_all('script')
            for script in scriptTags:
                scripts.append(script.get('href'))
            linkTags = beautifulSoup.find_all('link')
            for link in linkTags:
                links.append(link.get('href'))
            if (len(metas) + len(scripts) + len(links)) / 300 < 17 / 100:
                return 1
            elif 17 / 100 <= (len(metas) + len(scripts) + len(links)) <= 81 / 100:
                return 0
            else:
                return -1
        except:
            return -1

    def serverFormHandler(self, beautifulSoup):
        try:
            if len(beautifulSoup.find_all('form', action=True)) == 0:
                return 1
            else:
                for form in beautifulSoup.find_all('form', action=True):
                    if form.get('action') == "" or form.get("action") == "about:blank":
                        return -1
                    elif self.url not in form.get('action') or re.findall(Pattern.DOMAIN, self.url)[0] not in form.get(
                            'action'):
                        return 0
                    else:
                        return 1
        except:
            return -1

    def submitMailInformation(self):
        try:
            resp = requests.get(self.url)
            if re.findall(r"[mail\(\)|mailto:?]", resp.text):
                return -1
            else:
                return 1
        except:
            return -1

    def abnormalURL(self, domain_info):
        domain = re.findall(Pattern.DOMAIN, self.url)[0]
        try:
            domainName = domain_info['domain_name']
            if type(domainName) == type("domain"):
                if domain == domainName.lower():
                    return 1
                else:
                    return -1
            else:
                if domain == domainName[1].lower():
                    return 1
                else:
                    return -1
        except:
            return -1
