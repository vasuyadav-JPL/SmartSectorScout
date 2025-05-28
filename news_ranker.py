from fetcher.rss_fetcher import fetch_articles
from ranker.hybrid_ranker import hybrid_rank_articles
from utils.classifier import classify_query

import cohere

co = cohere.Client("xz4U6TztdMHfFCH2ypgDnGZRNmBqZJbQvDzZI0rb")

def main():
    query = input("Enter your query: ").strip()
    category = classify_query(query)
    print(f"\n[Info] Query classified under category: {category}")

    articles = fetch_articles(query, category)
    print(f"[Debug] Collected {len(articles)} valid articles containing the query.")

    if not articles:
        print("\n[Warning] No valid articles found containing the query.")
    else:
        ranked_articles = hybrid_rank_articles(query, articles, co)
        print(f"\nTop {len(ranked_articles)} trending news articles about '{query}':\n")
        for idx, (score, article) in enumerate(ranked_articles, 1):
            print(f"{idx}. {article['title']}")
            print(f"   URL: {article['url']}")
            print(f"   Relevance Score: {score:.4f}\n")

if __name__ == "__main__":
    main()
