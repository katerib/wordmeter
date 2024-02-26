from flask import Flask, render_template, request, redirect, url_for 
from werkzeug.utils import secure_filename 
import os, PyPDF2, csv
from analyze import analyze_text
from helpers import process_file, process_text, allowed_file

app = Flask(__name__)
UPLOADS_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOADS_FOLDER

os.makedirs(UPLOADS_FOLDER, exist_ok=True)

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check whether the post request has the file part
        file = request.files.get('file')
        text_input = request.form.get('textinput')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            # Process the uploaded file
            texts = process_file(file_path, file_type=file.filename.rsplit('.', 1)[1].lower())

        elif text_input:
            print("Text")
            # Process the input text
            texts = [text_input]
        else:
            return render_template('upload.html', error="No file or input text provided.")

        analysis_results = {}
        for text in texts:
            word_counts, ngram_counts, ngrams = analyze_text(text)  # Call the analyze_text function
            analysis_results.update(ngrams)

        return render_template('results.html', 
            analysis_results=analysis_results)
        
    return render_template('upload.html')


if __name__ == "__main__":
    app.run(debug=True)
