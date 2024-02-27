from flask import Flask, render_template, request, redirect, url_for 
from werkzeug.utils import secure_filename 
import os, csv
from analyze import analyze_text
from helpers import process_file, process_text, allowed_file

app = Flask(__name__)
UPLOADS_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOADS_FOLDER

os.makedirs(UPLOADS_FOLDER, exist_ok=True)

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        text_input = request.form.get('textinput')

        # Advanced search options
        ngram_lengths = request.form.getlist('ngram_length')  # Returns a list of selected n-gram lengths
        ngram_lengths = [int(length) for length in ngram_lengths] if ngram_lengths else [2, 3, 4, 5]  # Default to all if none selected
        freq_target = int(request.form.get('freq_target', 2))  # Default to 2 if not specified

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            texts = process_file(file_path, file_type=file.filename.rsplit('.', 1)[1].lower())
        elif text_input:
            texts = [text_input]
        else:
            return render_template('upload.html', error="No file or input text provided.")

        analysis_results = {}
        for text in texts:
            # Adjust analyze_text function call to include new parameters
            word_counts, ngram_counts, ngrams = analyze_text(text, ngram_lengths, freq_target)
            analysis_results.update(ngrams)

        return render_template('results.html', analysis_results=analysis_results)
        
    return render_template('upload.html')


if __name__ == "__main__":
    app.run(debug=True)
