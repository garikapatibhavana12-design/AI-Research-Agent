def summarize_research(research_text):

    lines = research_text.split("\n")

    important_lines = []

    for line in lines:

        cleaned_line = line.strip()

        if cleaned_line != "":

            if (
                "QUERY:" not in cleaned_line
                and "RESEARCH ANALYSIS" not in cleaned_line
                and "RESEARCH STRUCTURE" not in cleaned_line
            ):
                important_lines.append(cleaned_line)

    summary_lines = important_lines[:10]

    summary = "\n".join(summary_lines)

    return summary

