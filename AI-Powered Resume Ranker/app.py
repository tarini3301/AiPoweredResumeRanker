from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from utils.pdf_reader import extract_text_from_pdf
from utils.preprocessor import preprocess
from utils.scorer import score_resume

UPLOAD_FOLDER = 'resumes'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        job_desc = request.form["job_description"]
        files = request.files.getlist("resumes")

        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        for file in files:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            raw_text = extract_text_from_pdf(file_path)
            cleaned = preprocess(raw_text)
            score = score_resume(cleaned, job_desc)
            results.append((filename, round(score * 100, 2)))

        results.sort(key=lambda x: x[1], reverse=True)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
