from News import NewsCategory
from News import KerbOnSecurityNews as kbs


# categories = NewsCategory.getCategory()
# print(categories.keys())
# category = "Web Fraud 2.0"
def getNews(category):
    a, b, c, d = kbs.getNews(category)
    news = kbs.generate_news_api(a, b, c, d, category)
    # print(type(news))
    return news
