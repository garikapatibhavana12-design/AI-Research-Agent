# 🤖 AI Research Agent

## Intelligent Research and Prompt Refinement Assistant

An AI-powered research assistant built using Python and Flask. The application analyzes user queries, refines prompts, retrieves relevant information from a knowledge base, summarizes research results, and evaluates the generated response.

---

## 🚀 Features

- 🔍 Prompt Analysis
- ✨ Prompt Refinement
- 📚 Knowledge Base Retrieval
- 🔎 Keyword-Based Information Retrieval
- 📝 Research Summarization
- 📊 Response Evaluation
- 📄 Structured Research Report
- 🌐 Web Interface using Flask

---

## ⚙️ Research Pipeline

User Query
↓
Prompt Analysis
↓
Prompt Refinement
↓
Knowledge Retrieval
↓
Research Generation
↓
Summarization
↓
Evaluation
↓
Final Research Report

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- Text Processing
- Keyword-Based Information Retrieval

---

## 📁 Project Structure

```text
AI_Research_Agent/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── knowledge_base.txt
│
├── modules/
│   ├── prompt_analysis.py
│   ├── prompt_refinement.py
│   ├── retrieval.py
│   ├── research.py
│   ├── summarizer.py
│   ├── evaluation.py
│   └── report_generator.py
│
├── templates/
│   ├── index.html
│   └── report.html
│
└── static/
    └── style.css
```

---

## ▶️ How to Run the Project

### Step 1: Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### Step 2: Navigate to the project folder

```bash
cd AI_Research_Agent
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the virtual environment

```bash
venv\Scripts\activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. The user enters a research query.
2. The system analyzes the query.
3. Important keywords and query complexity are identified.
4. The prompt is refined into a structured research request.
5. Relevant information is retrieved from the knowledge base.
6. The research content is organized.
7. Important information is summarized.
8. The response is evaluated.
9. A structured research report is displayed.

---

## 🔮 Future Improvements

- Vector embeddings
- Semantic search
- Full Retrieval-Augmented Generation (RAG)
- Integration with an LLM API
- Larger document knowledge base
- PDF report generation
- User authentication
- Research history

---

## 👩‍💻 Author

Garikapati Bhavana

---

## ⭐ Project Goal

The goal of this project is to demonstrate a modular research pipeline using Python, text processing, information retrieval, prompt engineering concepts, and a web-based interface.
