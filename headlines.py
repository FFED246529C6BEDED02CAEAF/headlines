import feedparser

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
         'cbs':'https://www.cbsnews.com/latest/rss/main'}

@app.route("/")

@app.route("/<publication>")

def get_news(publication="cnw"):
    feed = feedparser.parse(feeds[publication])
    first_article = feed['entries'][0]
    return """<html>
            <body>
                <h1>Today's Headlines </h1>
                <b>{0}</b> </br>
                <i>{1}<i/> </br>
                <p>{2}</p> </br>
            </body>
            <html>""".format(first_article.get("title"), first_article.
get("published"), first_article.get("summary"))

if __name__ == '__main__':
    app.run(port=5000, debug=True)