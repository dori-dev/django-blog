"""news reader
"""
import datetime
import requests
import json
from django.contrib.humanize.templatetags import humanize
from django.utils.translation import gettext as _

iran_standard_time = datetime.timedelta(hours=3, minutes=30)


def connect_web(url):
    data_param = {
        'rss_url': 'https://www.irna.ir/rss',
        'api_key': "yursdfbqcjdny9ogwzbrlgdhscwvwa9aqzypmsn1",
        'count': 50,
    }

    try:
        r = requests.post(url, timeout=60, data=data_param)
        if r.status_code == 200:
            return r.content
        return None
    except Exception as e:
        print(repr(e))
        return None


def parse_content(content):
    data = json.loads(content)
    articles = data['items']
    articles_dict = []
    for article in articles:
        try:
            title = article["title"]
            link = article["link"]
            desc = article["description"]
            date = article["pubDate"]
            date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            date = humanize.naturaltime(date + iran_standard_time)
            date = date.replace(",", " and").replace(
                ".", "").replace("،", " and ")
            date = " ".join(_(word) for word in date.split())
            img = article["enclosure"]["link"]
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
    web_url = "https://api.rss2json.com/v1/api.json"
    content = connect_web(web_url)
    return parse_content(content)


if __name__ == "__main__":
    print(main())
