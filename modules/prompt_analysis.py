def analyze_prompt(prompt):

    words = prompt.split()
    word_count = len(words)

    keywords = []

    for word in words:
        cleaned_word = word.lower().strip(".,?!")

        if len(cleaned_word) > 4:
            keywords.append(cleaned_word)

    if "explain" in prompt.lower():
        query_type = "Explanation"

    elif "compare" in prompt.lower():
        query_type = "Comparison"

    elif "advantages" in prompt.lower():
        query_type = "Advantages and Disadvantages"

    elif "how" in prompt.lower():
        query_type = "How-To Question"

    else:
        query_type = "General Research"

    if word_count <= 5:
        complexity = "Simple"
    elif word_count <= 15:
        complexity = "Medium"
    else:
        complexity = "Complex"

    return {
        "word_count": word_count,
        "keywords": keywords[:10],
        "query_type": query_type,
        "complexity": complexity,
        "original_prompt": prompt
    }

