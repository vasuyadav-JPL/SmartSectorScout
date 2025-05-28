import feedparser
from newspaper import Article
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils.config.rss_feeds import rss_feeds



def is_valid_article(article, query):
    text = article.text.lower()
    return query.lower() in text and len(text.split()) >= 100


def fetch_article_rss(entry, query):
    try:
        url = entry.link
        article = Article(url)
        article.download()
        article.parse()
        if is_valid_article(article, query):
            return {
                'title': article.title,
                'url': url,
                'text': article.text
            }
    except:
        return None


def fetch_articles(query, category):
    all_articles = []
    seen_urls = set()
    article_entries = []

    for feed_url in rss_feeds.get(category, []):
        try:
            feed = feedparser.parse(feed_url)
            article_entries.extend(feed.entries[:10])
        except:
            continue

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(fetch_article_rss, entry, query)
            for entry in article_entries
            if entry.link not in seen_urls and not seen_urls.add(entry.link)
        ]
        for future in as_completed(futures):
            article_data = future.result()
            if article_data:
                all_articles.append(article_data)

    return all_articles
