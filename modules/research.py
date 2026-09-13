from modules.retrieval import retrieve_information


def research_topic(prompt):

    results = retrieve_information(prompt)

    if not results:

        retrieved_information = (
            "No relevant information was found "
            "in the current knowledge base."
        )

    else:

        retrieved_information = ""

        for index, result in enumerate(results, start=1):

            retrieved_information += (
                f"\nSOURCE {index} "
                f"(Relevance Score: {result['score']})\n"
            )

            retrieved_information += (
                result["content"] + "\n"
            )

    research_result = f"""
RESEARCH ANALYSIS

QUERY:
{prompt}

RETRIEVED KNOWLEDGE:
{retrieved_information}

RESEARCH FRAMEWORK:

• Introduction
• Key Concepts
• Applications
• Advantages
• Challenges
• Future Scope
"""

    return research_result



