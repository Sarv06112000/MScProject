from AddressBarBasedFeatures import AddressFeatures
from AbnormalBasedFeatures import AbnormalFeatures
from DomainBasedFeatures import DomainFeatures
from HtmlAndJavaScriptBasedFeatures import HtmlJsFeatures
import whois
import WebCrawling as web


class FeaturesExtraction:
    def __init__(self, url):
        self.url = url
        try:
            self.domain_info = whois.whois(url)
        except:
            self.domain_info = 1
        self.soup = web.getSoup(url)
        self.address = AddressFeatures.AddressFeatures(self.url)
        self.abnormal = AbnormalFeatures.AbnormalFeatures(self.url)
        self.domain = DomainFeatures.DomainFeatures(self.url)
        self.htmljs = HtmlJsFeatures.HtmlJsFeatures(self.url)

    def getFeatures(self):
        features = [self.address.usingIPAddress(),
                    self.address.longURL(),
                    self.address.tinyURL(),
                    self.address.atRateSymbol(),
                    self.address.redirectDoubleSlash(),
                    self.address.prefixSuffixDomain(),
                    self.address.subMultiDomain(),
                    self.address.httpsDomain(self.domain_info),
                    self.address.domainRegLength(self.domain_info),
                    self.address.faviconExternalDomain(self.soup),
                    # self.address.nonStandardPort(),
                    self.address.httpsDomain(self.domain_info),
                    self.abnormal.requestURL(self.soup),
                    self.abnormal.urlOfAnchor(self.soup),
                    self.abnormal.linksInTags(self.soup),
                    self.abnormal.serverFormHandler(self.soup),
                    self.abnormal.submitMailInformation(),
                    self.abnormal.abnormalURL(self.domain_info)]
                    # self.htmljs.websiteForwarding(),
                    # self.htmljs.statusBarCustom(),
                    # self.htmljs.disableRightClick(),
                    # self.htmljs.usingPopUpWindow(),
                    # self.htmljs.iFrameRedirection(),
                    # self.domain.ageOfDomain(),
                    # self.domain.dnsRecord(),
                    # self.domain.websiteTraffic(),
                    # self.domain.pageRank(),
                    # self.domain.googleIndex(),
                    # self.domain.linkPointingPage(),
                    # self.domain.statisticReport()]
        return features


# url = "http://www.hud.ac.uk/students/"
# url = "http://www.Confirme-paypal.com/"
# url = "http://www.legitimate.com//http://www.phishing.com"
# url = "http://bit.ly/19DXSk4"
# url = "http://portal.hud.ac.uk/"
# url = "http://federmacedoadv.com.br/3f/aze/ab51e2e319e51502f416dbe46b773a5e/?cmd=_home&amp;dispatch=11004d58f5b74f8dc1e7c2e8dd4105e811004d58f5b74f8dc1e7c2e8dd4105e8@phishing.website.html"
# url = "http://127.0.0.1/fake.html"
# url = "http://0x58.0xCC.0xCA.0x62/2/paypal.ca/index.html"
# url = "https://www.tutorialspoint.com/python-pandas-get-the-number-of-days-from-timedelta"
url = "https://www.google.com/search?q=google+maps&rlz=1C1CHBD_enIN1043IN1043&oq=go&aqs=chrome.4.69i60j46i131i199i433i465i512j0i131i433i512j69i57j0i433i512l2j69i60l2.2648j0j7&sourceid=chrome&ie=UTF-8"


fe = FeaturesExtraction(url)
print(fe.getFeatures())
