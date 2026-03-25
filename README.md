# Composable LLM Pipeline using LCEL

This project demonstrates how to build a modular and composable LLM pipeline using LangChain Expression Language (LCEL).

The application exposes an API using FastAPI and LangServe, allowing dynamic execution of LLM tasks such as translation, summarization, and explanation.

---

## 🚀 Features

- LCEL chaining (`prompt | model | parser`)
- Dynamic task-based prompting
- FastAPI backend
- LangServe integration for API exposure
- Groq LLM (Gemma model)

---

## 🧠 Key Concept

This project focuses on **composability**, where different components (prompt, model, parser) are combined to form reusable pipelines.

---

## 📁 Project Structure

```
composable-llm-pipeline-lcel/
├── app/
│   └── main.py
├── notebooks/
│   └── lcel_experiments.ipynb
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Setup

```bash
git clone https://github.com/shaik-zaid/composable-llm-pipeline-lcel
cd composable-llm-pipeline-lcel

# create environment
conda create -p .venv python=3.10 -y

# activate environment (Windows)
conda activate .venv/

# or (Linux/Mac)
conda activate .venv

pip install -r requirements.txt
```

---

## ▶️ Run the API

```bash
# Option 1 (recommended)
uvicorn app.main:app --reload

# Option 2
python app/main.py
```

Open in browser:  
http://127.0.0.1:8000/docs  

---

## 🧪 Example Input

```json
{
  "input": {
    "task": "Translate to French",
    "text": "Hello"
  }
}
```

---

## 🛠 Tech Stack

- LangChain (LCEL)
- Groq
- FastAPI
- LangServe