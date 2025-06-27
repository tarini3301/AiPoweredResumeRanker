# AI-Powered Resume Ranker 🚀

An AI-powered web application that ranks resumes for a specific job profile using Natural Language Processing (NLP) techniques.

## 📜 Objective
Automate the resume screening process by ranking resumes based on their relevance to the job description using NLP, TF-IDF, and cosine similarity.

## 🧠 Features
- Upload multiple PDF resumes
- Upload a job description
- Extract and preprocess text using **SpaCy**
- Vectorize text using **TF-IDF**
- Compute similarity scores between resumes and the job description
- Rank candidates based on relevance
- Download a ranked report as CSV for HR

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, Bootstrap (via Flask templates)
- **Backend:** Python, Flask
- **NLP:** SpaCy
- **Machine Learning:** Scikit-learn (TF-IDF Vectorizer)
- **File Handling:** pdfminer, PyPDF2 or similar

---

## 🔧 Installation

### Prerequisites:
- Python 3.7+
- pip

### Clone the repository:
```bash
git clone https://github.com/your-username/AiPoweredResumeRanker.git
cd AiPoweredResumeRanker
