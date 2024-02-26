import io, os, csv
import fitz                     # aka pymupdf


from analyze import analyze_text

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_pdf(file_path):
    try:
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return [text]
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return []


def process_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as txtfile:
        text = txtfile.read()
    return [text]


def process_file(file_path, file_type):
    path, extension = os.path.splitext(file_path)

    print(f"extension: {extension}\nfile path: {file_path}\nfile type: {file_type}\n _: {path}")
    
    if extension == '.pdf':
        print('Processing PDF')
        text = process_pdf(file_path)
    elif extension == '.txt':
        print('Processing TXT')
        text = process_text_file(file_path)
    elif file_type == 'csv':
        print('Processing CSV')
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            texts = [' '.join(row) for row in reader]
        return texts
    return text


def process_text(text):
    """
    placeholder for addt'l text
    """
    return text


if __name__ == "__main__":
    file = 'ignore\sampleParagraph.pdf'
    text = process_file(file, '.pdf')
    narrowed_word_counts, narrowed_ngram_counts, narrowed_filtered_ngrams = analyze_text(text)
    print(narrowed_filtered_ngrams)
    print(narrowed_word_counts)