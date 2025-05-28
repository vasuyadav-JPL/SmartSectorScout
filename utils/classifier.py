def classify_query(query):
    # Basic keyword-based classifier (you can improve this later)
    query = query.lower()
    if "energy" in query or "climate" in query:
        return "renewable_energy"
    elif "stock" in query or "investment" in query or "finance" in query:
        return "finance"
    elif "health" in query or "medicine" in query:
        return "healthcare"
    elif "technology" in query or "tech" in query:
        return "technology"
    elif "e-commerce" in query or "amazon" in query:
        return "ecommerce"
    elif "car" in query or "automobile" in query:
        return "automotive"
    elif "real estate" in query or "property" in query:
        return "real_estate"
    elif "fmcg" in query:
        return "fmcg"
    elif "construction" in query or "infrastructure" in query:
        return "construction"
    elif "sports" in query:
        return "sports"
    else:
        return "technology"  # default fallback
