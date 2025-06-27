import pickle
from sklearn.metrics.pairwise import cosine_similarity

def score_resume(resume_text, job_desc_text):
    with open("model/tfidf_vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    vectors = vectorizer.transform([resume_text, job_desc_text])
    return cosine_similarity(vectors[0], vectors[1])[0][0]
