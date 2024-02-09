import feedparser

from flask import render_template
from flask import Flask
app = Flask(__name__)

feeds = {'complex': 'https://www.complex.com/index.xml',
         'nyt':'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
         'aljazeera':'https://www.aljazeera.com/xml/rss/all.xml',
         'politico':'https://www.politico.com/rss/politicopicks.xml',
         'ft':'https://www.ft.com/rss/home',
         'bd':'https://www.businessdailyafrica.com/service/rss/bd/1939132/feed.rss',
         'cnw':'https://www.celebritynetworth.com/category/articles/feed/',
         'sky':'https://feeds.skynews.com/feeds/rss/technology.xml',
         'cbs':'https://www.cbsnews.com/latest/rss/main',
         'pulse':'https://www.pulselive.co.ke/rss',
         'topstories':'https://abcnews.go.com/abcnews/topstories',
         'usheadlines':'https://abcnews.go.com/abcnews/usheadlines',
         'internationalheadlines':'https://abcnews.go.com/abcnews/internationalheadlines',
         'politicsheadlines':'https://abcnews.go.com/abcnews/politicsheadlines',
         'moneyheadline':'https://abcnews.go.com/abcnews/moneyheadlines',
         'celebrity':'https://www.buzzfeed.com/celebrity.xml',
         'tvandmovies':'https://www.buzzfeed.com/tvandmovies.xml',
         'reader':'https://www.buzzfeed.com/reader.xml',
         'spm':'https://spmbuzz.com/feed/',
         }

@app.route("/")
@app.route("/<publication>")
def get_news(publication="complex"):
    feed = feedparser.parse(feeds[publication])
    first_article = feed['entries'][0]
    render_template("home.html",title=first_article.get("title"),published=first_article.get("published"),summary=first_article.get("summary")).format(first_article.get("title"), first_article.
get("published"), first_article.get("summary"))

if __name__ == '__main__':
    app.run(port=5000, debug=True)