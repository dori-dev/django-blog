"""
تیتر
عکس
زمان
خلاصه

با کلیک بر روی تیتر یا عکس(کلا اون ناحیه)
به اصل خبر در ایرنا برود
"""
import datetime
import requests
from bs4 import BeautifulSoup
from django.contrib.humanize.templatetags import humanize
from django.utils.translation import gettext as _

iran_standard_time = datetime.timedelta(hours=3, minutes=30)


def connect_web(url):
    try:
        r = requests.get(url, timeout=60)
        if r.status_code == 200:
            return r.content
        return
    except Exception as e:
        print(repr(e))


def parse_content(content):
    soup = BeautifulSoup(content, "xml")
    articles = soup.findAll("item")
    articles_dict = []
    for article in articles:
        try:
            title = article.find("title").text
            link = article.find("link").text
            desc = article.find("description").text
            date = article.find("pubDate").text
            date = date.split(",")[1][1:-4]
            date = datetime.datetime.strptime(date, "%d %b %Y %H:%M:%S")
            date = humanize.naturaltime(date + iran_standard_time)
            date = date.replace(",", " and").replace(
                ".", "").replace("،", " and ")
            date = " ".join(_(word) for word in date.split())

            img = article.find("enclosure", url=True)['url']
            articles_dict.append(
                {
                    "title": title,
                    "link": link,
                    "desc": desc,
                    "date": date,
                    "img": img
                }
            )
        except Exception as e:
            print(repr(e))
    return articles_dict


def main():
    web_url = "https://www.irna.ir/rss"
    content = connect_web(web_url)
    return parse_content(content)


if __name__ == "__main__":
    print(main())
