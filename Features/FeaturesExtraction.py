from Features.AddressBarBasedFeatures.AddressFeatures import AddressFeatures
from Features.AbnormalBasedFeatures.AbnormalFeatures import AbnormalFeatures
from Features.DomainBasedFeatures.DomainFeatures import DomainFeatures
from Features.HtmlAndJavaScriptBasedFeatures.HtmlJsFeatures import HtmlJsFeatures
import whois
from Features import WebCrawling as web


class FeaturesExtraction:
    def __init__(self, url):
        self.url = url
        try:
            self.domain_info = whois.whois(url)
        except:
            self.domain_info = 1
        self.response = web.getResponse(url)
        self.soup = web.getSoup(self.response)
        self.address = AddressFeatures(self.url)
        self.abnormal = AbnormalFeatures(self.url)
        self.domain = DomainFeatures(self.url)
        self.htmljs = HtmlJsFeatures(self.url)

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
                    self.address.nonStandardPort(),
                    self.address.httpsDomain(self.domain_info),
                    self.abnormal.requestURL(self.soup),
                    self.abnormal.urlOfAnchor(self.soup),
                    self.abnormal.linksInTags(self.soup),
                    self.abnormal.serverFormHandler(self.soup),
                    self.abnormal.submitMailInformation(self.response),
                    self.abnormal.abnormalURL(self.domain_info),
                    self.htmljs.websiteForwarding(),
                    self.htmljs.statusBarCustom(self.response),
                    self.htmljs.disableRightClick(self.response),
                    self.htmljs.usingPopUpWindow(self.response),
                    self.htmljs.iFrameRedirection(self.response),
                    self.domain.ageOfDomain(self.domain_info),
                    self.domain.dnsRecord(self.domain_info),
                    self.domain.websiteTraffic(),
                    self.domain.pageRank(self.soup),
                    self.domain.googleIndex(),
                    self.domain.linkPointingPage(self.soup),
                    self.domain.statisticReport()]
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
# url = "https://www.google.com/maps"
# url = "https://157.240.16.35"

