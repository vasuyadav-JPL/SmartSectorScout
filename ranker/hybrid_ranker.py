from numpy import dot
from numpy.linalg import norm


def hybrid_rank_articles(query, articles, co, alpha=0.5):
    query_embed = co.embed(
        texts=[query],
        input_type="search_query",
        model="embed-english-v3.0"
    ).embeddings[0]

    doc_texts = [a['text'] for a in articles]
    doc_embeds = co.embed(
        texts=doc_texts,
        input_type="search_document",
        model="embed-english-v3.0"
    ).embeddings

    ranked = []
    query_terms = query.lower().split()

    for i, article in enumerate(articles):
        bm25_score = sum(article['text'].lower().count(term) for term in query_terms)
        cos_sim = dot(query_embed, doc_embeds[i]) / (norm(query_embed) * norm(doc_embeds[i]))
        final_score = alpha * bm25_score + (1 - alpha) * cos_sim
        ranked.append((final_score, article))

    if ranked:
        max_score = max(ranked, key=lambda x: x[0])[0]
        min_score = min(ranked, key=lambda x: x[0])[0]
        score_range = max_score - min_score if max_score != min_score else 1.0
        ranked = [((score - min_score) / score_range, art) for score, art in ranked]

    ranked.sort(reverse=True, key=lambda x: x[0])
    return ranked[:10]
