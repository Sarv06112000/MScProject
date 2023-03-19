from AddressBarBasedFeatures import AddressFeatures
from AbnormalBasedFeatures import AbnormalFeatures
from DomainBasedFeatures import DomainFeatures
from HtmlAndJavaScriptBasedFeatures import HtmlJsFeatures


class FeaturesExtraction:
    def __init__(self, url):
        self.url = url
        self.address = AddressFeatures(url)
        self.abnormal = AbnormalFeatures(url)
        self.domain = DomainFeatures(url)
        self.htmljs = HtmlJsFeatures(url)

    def getFeatures(self, url):
        features = [self.address.usingIPAddress(url),
                    self.address.longURL(url),
                    self.address.tinyURL(url),
                    self.address.atRateSymbol(url),
                    self.address.redirectDoubleSlash(url),
                    self.address.prefixSuffixDomain(url),
                    self.address.subMultiDomain(url),
                    self.address.httpsDomain(url),
                    self.address.domainRegLength(url),
                    self.address.faviconExternalDomain(url),
                    self.address.nonSandardPort(url),
                    self.address.httpsInDomain(url),
                    self.abnormal.requestURL(url),
                    self.abnormal.urlOfAnchor(url),
                    self.abnormal.linksInTags(url),
                    self.abnormal.serverFormHandler(url),
                    self.abnormal.submitMailInformation(url),
                    self.abnormal.abnormalURL(url),
                    self.htmljs.websiteForwarding(url),
                    self.htmljs.statusBarCustom(url),
                    self.htmljs.disableRightClick(url),
                    self.htmljs.usingPopUpWindow(url),
                    self.htmljs.iFrameRedirection(url),
                    self.domain.ageOfDomain(url),
                    self.domain.dnsRecord(url),
                    self.domain.websiteTraffic(url),
                    self.domain.pageRank(url),
                    self.domain.googleIndex(url),
                    self.domain.linkPointingPage(url),
                    self.domain.statisticsReport(url)]
        return features
