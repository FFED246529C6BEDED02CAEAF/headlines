import feedparser

from flask import render_template
from flask import Flask
app = Flask(__name__)

feeds = {'ke':'https://www.kenyans.co.ke/feeds/news/all',
    'politco':'https://www.politico.com/rss/politicopicks.xml',
         'complex': 'https://www.complex.com/index.xml',
         'nytimes':'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
         'aljazeera':'https://www.aljazeera.com/xml/rss/all.xml',
         'ft':'https://www.ft.com/rss/home',
         'bd':'https://www.businessdailyafrica.com/service/rss/bd/1939132/feed.rss',
         'celeb-net':'https://www.celebritynetworth.com/category/articles/feed/',
         'sky-tech':'https://feeds.skynews.com/feeds/rss/technology.xml',
         'cbs':'https://www.cbsnews.com/latest/rss/main',
         'pulse':'https://www.pulselive.co.ke/rss',
         'abc-top':'https://abcnews.go.com/abcnews/topstories',
         'us-headlines':'https://abcnews.go.com/abcnews/usheadlines',
         'abc-int':'https://abcnews.go.com/abcnews/internationalheadlines',
         'abc-pol':'https://abcnews.go.com/abcnews/politicsheadlines',
         'abc-money':'https://abcnews.go.com/abcnews/moneyheadlines',
         'bf-celeb':'https://www.buzzfeed.com/celebrity.xml',
         'bf-movies':'https://www.buzzfeed.com/tvandmovies.xml',
         'bfread':'https://www.buzzfeed.com/reader.xml',
         'spm':'https://spmbuzz.com/feed/',
         'wiredculture':'https://www.wired.com/feed/category/culture/latest/rss',
         'wiredbs':'https://www.wired.com/feed/category/business/latest/rss',
         'wiredgear':'https://www.wired.com/feed/category/gear/latest/rss',
         'wiredsci':'https://www.wired.com/feed/category/science/latest/rss',
         'etgallery':'https://www.etonline.com/gallery/rss',
         'etlifestyle':'https://www.etonline.com/style/lifestyle/rss',
         'etmusic':'https://www.etonline.com/music/rss',
         'thevergecreator':'https://www.theverge.com/rss/creators/index.xml',
         'thevergecyber':'https://www.theverge.com/rss/cyber-security/index.xml',
         'thevergefilm':'https://www.theverge.com/rss/film/index.xml',
         'thevergesci':'https://www.theverge.com/rss/science/index.xml',
         'thevergespace':'https://www.theverge.com/rss/space/index.xml',
         'tuko':'https://www.tuko.co.ke/rss/all.rss',
         'thevergestreaming-wars':'https://www.theverge.com/rss/streaming-wars/index.xml',
         'wiredai':'https://www.wired.com/feed/tag/ai/latest/rss'}

@app.route("/")
@app.route("/<publication>")

def get_news(publication="kenyans"):
    feed = feedparser.parse(feeds[publication])
    first_article = feed['entries'][0]
    return render_template("home.html",
                           title=first_article.get("title"),
                           published=first_article.get("published"),
                           summary=first_article.get("summary"))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
