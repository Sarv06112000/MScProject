from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()
url = "https://krebsonsecurity.com/category/data-breaches/"
response = http.request('GET',url)
soup = BeautifulSoup(response.data, 'html.parser')

def getCategory():
    category = dict()
    category_anchors = soup.findAll('a', attrs={'rel':'category tag'})
    for category_anchor in category_anchors:
        category[category_anchor.text]=category_anchor.get('href')
    return category

def getCategoryTags():
    category_tag = dict()
    category_anchors_tags = soup.findAll('a', attrs={'rel':'tag'})
    for category_anchor_tag in category_anchors_tags:
        category_tag[category_anchor_tag.text]=category_anchor_tag.get('href')
    return category_tag

# print(getCategory())
# print(getCategoryTags())
# for i,j in getCategoryTags().items():
#     print(i,j)
