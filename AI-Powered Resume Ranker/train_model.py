import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from utils.pdf_reader import extract_text_from_pdf
from utils.preprocessor import preprocess

texts = []

for file in os.listdir("training_resumes"):
    if file.endswith(".pdf"):
        path = os.path.join("training_resumes", file)
        raw_text = extract_text_from_pdf(path)
        cleaned = preprocess(raw_text)
        texts.append(cleaned)

vectorizer = TfidfVectorizer()
vectorizer.fit(texts)

os.makedirs("model", exist_ok=True)
with open("model/tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Vectorizer trained and saved to model/tfidf_vectorizer.pkl")
