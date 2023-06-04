from bs4 import BeautifulSoup
from News import NewsCategory
import urllib3


def getNews(category):
    cat = category
    http = urllib3.PoolManager()
    category = NewsCategory.getCategory()
    # print(category)
    url = category.get(cat)
    # response = http.request('GET', 'https://krebsonsecurity.com/category/data-breaches/')
    # print(url)
    response = http.request("GET", url)
    data = response.data
    soup = BeautifulSoup(data, 'html.parser')
    # print(soup.prettify())

    urls = set()
    headlines = set()
    news_Articles = set()
    news_images = set()

    div_tags_excerpt = soup.findAll('div', attrs={'class': 'excerpt-thumb'})
    for div_tag_excerpt in div_tags_excerpt:
        anchors = soup.findAll('a', attrs={'rel': 'bookmark'})
        for anchor in anchors:
            urls.add(anchor.get('href'))
            headlines.add(anchor.get('title'))
            imgs_tags = anchor.findAll('img')
            for img_tag in imgs_tags:
                news_images.add(img_tag.get('src'))

    div_tags_entry = soup.findAll('div', attrs={'class': 'entry-summary'})
    for div_tag_entry in div_tags_entry:
        p_tags = div_tag_entry.findAll('p')
        for p_tag in p_tags:
            news_Articles.add(p_tag.text)

    urls = list(urls)
    headlines = list(headlines)
    news_Articles = list(news_Articles)
    news_images = list(news_images)
    img_src = ""
    if len(urls) < len(news_Articles):
        for i in range(len(urls), len(news_Articles)):
            urls.append(str(url))
    if len(headlines) < len(news_Articles):
        headline = cat
        for i in range(len(headlines), len(news_Articles)):
            headlines.append(str(headline))
    if len(news_images) < len(news_Articles):
        for i in range(len(news_images), len(news_Articles)):
            news_images.append(str(img_src))

    return urls, headlines, news_Articles, news_images


# urls, headlines, news_Articles, news_images, category = getNews(category)

def generate_news_api(urls, headlines, news_Articles, news_images, category):
    articles = list()
    for i in range(0, len(urls)):
        articles.append(dict(url=urls[i], title=headlines[i], description=news_Articles[i], urlToImage=news_images[i]))

    news = {"totalResults": len(news_Articles), "category": category, "articles": articles}
    return news


"""
if(len(urls) == len(headlines) == len(news_Articles) == len(news_images)):
    print(generate_news_api(urls, headlines, news_Articles, news_images))
else:
    news_images.append(img_src)
    print(generate_news_api(urls, headlines, news_Articles, news_images))
"""
