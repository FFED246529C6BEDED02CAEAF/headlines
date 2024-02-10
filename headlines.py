import feedparser

from flask import render_template
from flask import Flask
app = Flask(__name__)
feeds = {'ptc':'https://www.politico.com/rss/politicopicks.xml',
         'cpl': 'https://www.complex.com/index.xml',
         'nyt':'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
         'alj':'https://www.aljazeera.com/xml/rss/all.xml',
         'ft':'https://www.ft.com/rss/home',
         'bd':'https://www.businessdailyafrica.com/service/rss/bd/1939132/feed.rss',
         'cnw':'https://www.celebritynetworth.com/category/articles/feed/',
         'sky':'https://feeds.skynews.com/feeds/rss/technology.xml',
         'cbs':'https://www.cbsnews.com/latest/rss/main',
         'pls':'https://www.pulselive.co.ke/rss',
         'top':'https://abcnews.go.com/abcnews/topstories',
         'ush':'https://abcnews.go.com/abcnews/usheadlines',
         'ihl':'https://abcnews.go.com/abcnews/internationalheadlines',
         'phl':'https://abcnews.go.com/abcnews/politicsheadlines',
         'mhl':'https://abcnews.go.com/abcnews/moneyheadlines',
         'clb':'https://www.buzzfeed.com/celebrity.xml',
         'tam':'https://www.buzzfeed.com/tvandmovies.xml',
         'read':'https://www.buzzfeed.com/reader.xml',
         'spm':'https://spmbuzz.com/feed/',
         'lt':'https://www.wired.com/feed/category/culture/latest/rss',
         'wbs':'https://www.wired.com/feed/category/business/latest/rss',
         'gear':'https://www.wired.com/feed/category/gear/latest/rss',
         'sci':'https://www.wired.com/feed/category/science/latest/rss',
         'et':'https://www.etonline.com/gallery/rss',
         'etl':'https://www.etonline.com/style/lifestyle/rss',
         'etm':'https://www.etonline.com/music/rss',
         'creator':'https://www.theverge.com/rss/creators/index.xml',
         'cyber':'https://www.theverge.com/rss/cyber-security/index.xml',
         'film':'https://www.theverge.com/rss/film/index.xml',
         'sci':'https://www.theverge.com/rss/science/index.xml',
         'space':'https://www.theverge.com/rss/space/index.xml',
         'tuko':'https://www.tuko.co.ke/rss/all.rss',
         'stm':'https://www.theverge.com/rss/streaming-wars/index.xml',
         'wai':'https://www.wired.com/feed/tag/ai/latest/rss'}

@app.route("/")
@app.route("/<publication>")

def get_news(publication="tuko"):
    feed = feedparser.parse(feeds[publication])
    first_article = feed['entries'][0]
    return render_template("home.html",
                           title=first_article.get("title"),
                           published=first_article.get("published"),
                           summary=first_article.get("summary"))

if __name__ == "__main__":
    app.run(port=5000, debug=True)