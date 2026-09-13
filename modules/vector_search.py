from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def split_text(text, chunk_size=150):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i : i + chunk_size])
        if chunk.strip():
            chunks.append(chunk)

    return chunks


def semantic_search(query, document_text, top_k=3):
    if not document_text:
        return []

    chunks = split_text(document_text)

    if not chunks:
        return []

    documents = [query] + chunks

    try:
        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform(documents)
    except ValueError:
        # Handles cases where documents contain only stop words or numbers
        return []

    query_vector = vectors[0]
    document_vectors = vectors[1:]

    similarity_scores = cosine_similarity(query_vector, document_vectors)[0]

    results = []
    for index, score in enumerate(similarity_scores):
        results.append(
            {"content": chunks[index], "score": round(float(score), 3)}
        )

    results.sort(key=lambda item: item["score"], reverse=True)

    return results[:top_k]
