def generate_report(
    user_prompt,
    refined_prompt,
    analysis,
    research_result,
    summary,
    evaluation
):

    report = {
        "title": "AI Research Report",
        "original_query": user_prompt,
        "refined_query": refined_prompt,
        "analysis": analysis,
        "research": research_result,
        "summary": summary,
        "evaluation": evaluation
    }

    return report
