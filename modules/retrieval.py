import os
import re


def retrieve_information(query):

    file_path = os.path.join("data", "knowledge_base.txt")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        return []

    query_words = re.findall(
        r"\b[a-zA-Z]{4,}\b",
        query.lower()
    )

    paragraphs = content.split("\n\n")

    scored_results = []

    for paragraph in paragraphs:

        paragraph_lower = paragraph.lower()

        score = 0

        for word in query_words:
            if word in paragraph_lower:
                score += 1

        if score > 0:
            scored_results.append(
                {
                    "content": paragraph.strip(),
                    "score": score
                }
            )

    scored_results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return scored_results[:3]
