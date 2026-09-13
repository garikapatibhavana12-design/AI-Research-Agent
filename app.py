import os
from flask import Flask, render_template, request
from PyPDF2 import PdfReader
from werkzeug.utils import secure_filename

# ==============================
# IMPORT PROJECT MODULES
# ==============================
from modules.evaluation import evaluate_response
from modules.prompt_analysis import analyze_prompt
from modules.prompt_refinement import refine_prompt
from modules.report_generator import generate_report
from modules.research import research_topic
from modules.summarizer import summarize_research
from modules.vector_search import semantic_search

# ==============================
# FLASK APPLICATION
# ==============================
app = Flask(__name__)

# ==============================
# UPLOAD CONFIGURATION
# ==============================
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"txt", "pdf"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder automatically
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ==============================
# RESEARCH HISTORY
# ==============================
research_history = []


# ==============================
# CHECK FILE TYPE
# ==============================
def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# ==============================
# READ TXT FILE
# ==============================
def read_txt_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except UnicodeDecodeError:
        with open(file_path, "r", encoding="latin-1") as file:
            return file.read()


# ==============================
# READ PDF FILE
# ==============================
def read_pdf_file(file_path):
    document_text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            document_text += page_text + "\n"
    return document_text


# ==============================
# HOME ROUTE
# ==============================
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_prompt = request.form.get("prompt", "").strip()

        # ==============================
        # GET UPLOADED DOCUMENT
        # ==============================
        uploaded_file = request.files.get("document")

        document_content = ""

        # ==============================
        # HANDLE FILE UPLOAD
        # ==============================
        if uploaded_file and uploaded_file.filename != "":
            if allowed_file(uploaded_file.filename):
                filename = secure_filename(uploaded_file.filename)
                file_path = os.path.join(
                    app.config["UPLOAD_FOLDER"], filename
                )

                # Save uploaded file
                uploaded_file.save(file_path)

                # Get file extension
                file_extension = filename.rsplit(".", 1)[1].lower()

                # Read TXT file
                if file_extension == "txt":
                    document_content = read_txt_file(file_path)

                # Read PDF file
                elif file_extension == "pdf":
                    document_content = read_pdf_file(file_path)

        # ==============================
        # PREVENT EMPTY INPUT
        # ==============================
        if not user_prompt:
            return render_template(
                "index.html", research_history=research_history
            )

        # ==============================
        # ADD QUERY TO HISTORY
        # ==============================
        research_history.insert(0, user_prompt)

        # Keep only latest 10 searches
        if len(research_history) > 10:
            research_history.pop()

        # ==============================
        # STEP 1: PROMPT ANALYSIS
        # ==============================
        analysis = analyze_prompt(user_prompt)

        # ==============================
        # STEP 2: PROMPT REFINEMENT
        # ==============================
        refined_prompt = refine_prompt(user_prompt)

        # ==============================
        # STEP 3: RESEARCH
        # ==============================
        research_result = research_topic(refined_prompt)

        # ==============================
        # SEMANTIC DOCUMENT SEARCH
        # ==============================
        semantic_results = []

        if document_content:
            semantic_results = semantic_search(
                user_prompt, document_content, top_k=3
            )

            if semantic_results:
                research_result += (
                    "\n\n"
                    "===== SEMANTICALLY RETRIEVED "
                    "DOCUMENT INFORMATION =====\n\n"
                )

                for result in semantic_results:
                    research_result += (
                        result["content"]
                        + "\n\n"
                        + "Relevance Score: "
                        + str(result["score"])
                        + "\n\n"
                    )

        # ==============================
        # STEP 4: SUMMARIZATION
        # ==============================
        summary = summarize_research(research_result)

        # ==============================
        # STEP 5: EVALUATION
        # ==============================
        evaluation = evaluate_response(summary)

        # ==============================
        # STEP 6: REPORT GENERATION
        # ==============================
        report = generate_report(
            user_prompt,
            refined_prompt,
            analysis,
            research_result,
            summary,
            evaluation,
        )

        # ==============================
        # DISPLAY REPORT
        # ==============================
        return render_template(
            "report.html",
            user_prompt=user_prompt,
            analysis=analysis,
            refined_prompt=refined_prompt,
            research_result=research_result,
            summary=summary,
            evaluation=evaluation,
            report=report,
            semantic_results=semantic_results,
        )

    # ==============================
    # GET REQUEST
    # ==============================
    return render_template("index.html", research_history=research_history)


# ==============================
# RUN APPLICATION
# ==============================
if __name__ == "__main__":
    app.run(debug=True)
    