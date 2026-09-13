def evaluate_response(summary):

    # Count total words
    word_count = len(summary.split())

    # Count total characters
    character_count = len(summary)

    # Count sentences
    sentence_count = len(
        [
            sentence
            for sentence in summary.split(".")
            if sentence.strip()
        ]
    )

    # Evaluate response quality
    if word_count >= 80:
        quality = "Detailed"
        score = "High"

    elif word_count >= 40:
        quality = "Good"
        score = "Medium"

    else:
        quality = "Basic"
        score = "Low"

    # Return evaluation results
    return {
        "word_count": word_count,
        "character_count": character_count,
        "sentence_count": sentence_count,
        "quality": quality,
        "score": score,
        "status": "Research Completed Successfully"
    }


