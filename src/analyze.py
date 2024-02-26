import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, ngrams, pos_tag
from collections import Counter

from posPatterns import POSPatterns
from sampleText import long_text, sentence 

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

FREQ_TARGET = 2

pos_patterns_instance = POSPatterns()
pos_patterns = pos_patterns_instance.get_pos_patterns()

def filter_ngrams_by_pos(ngram_counts):
    """
    Filter n-grams by desired part-of-speech patterns, considering only patterns up to a specified length.

    Purpose: narrow down the list of identified n-grams to those that match a specific POS pattern. 

    Parameters:
    - ngram_counts (dict): Dictionary of n-gram counts.
    - pos_patterns_by_length (dict): Dict of POS patterns organized by length.

    Returns:
        - dict: A dictionary with the same structure as ngram_counts, but filtered by the specified POS patterns.
    """
    filtered_ngram_counts = {}

    for n, counts in ngram_counts.items():
        for ngram, count in counts.items():
            tags = pos_tag(ngram)
            pos_pattern = tuple(tag for _, tag in tags)
            # Check if the POS pattern of this n-gram matches any desired pattern
            if pos_pattern in pos_patterns[n]:
                if n not in filtered_ngram_counts:
                    filtered_ngram_counts[n] = Counter()
                # Construct the phrase from the n-gram
                phrase = ' '.join(ngram)
                # Add the phrase and its count to the filtered results
                filtered_ngram_counts[n][phrase] += count
    return filtered_ngram_counts



def count_ngrams(words, max_n):
    ngram_counts = {}
    for n in range(2, max_n + 1):
        n_grams = list(ngrams(words, n))
        ngram_counts[n] = Counter(n_grams)
    return ngram_counts


def process_text(text, max_n=5):
    stop_words = set(stopwords.words('english'))
    if isinstance(text, list):  # handle cases where text is a list by joining elements into a single string
        text = ' '.join(text)
    words = word_tokenize(text.lower())
    words_filtered = [word for word in words if word.isalpha() and word not in stop_words]
    word_counts = Counter(words_filtered)
    ngram_counts = count_ngrams(words, max_n)
    return word_counts, ngram_counts


def narrow_by_type(source, type=None):
    """
    Narrows results by eliminating any word/n-gram with a frequency <= {FREQ_TARGET}, declared globally. 
    """
    results = {}
    if type is None:
        return results
    if type == 'word':
        # Direct filtering for word_counts
        results = {string: count for string, count in source.items() if count >= FREQ_TARGET}
    elif type == 'ngram' or type == 'filtered_ngrams':
        # Handle nested Counters for ngram_counts and filtered_ngrams
        for n, counts in source.items():
            filtered_counts = {ngram: count for ngram, count in counts.items() if count >= FREQ_TARGET}
            if filtered_counts:
                results[n] = filtered_counts
    return results

def narrow_results(word_counts, ngram_counts, filtered_ngrams):
    narrowed_word_counts = narrow_by_type(word_counts, type='word')
    narrowed_ngram_counts = narrow_by_type(ngram_counts, type='ngram')
    narrowed_filtered_ngrams = narrow_by_type(filtered_ngrams, type='filtered_ngrams')

    return narrowed_word_counts, narrowed_ngram_counts, narrowed_filtered_ngrams


def analyze_text(text):
    """
    Master function that handles analysis and filtering of words and ngrams for provided text.
    """
    if not text:
        return None
    
    try:
        word_counts, ngram_counts = process_text(text, 5)
        filtered_ngrams = filter_ngrams_by_pos(ngram_counts)
        
        narrowed_word_counts, narrowed_ngram_counts, narrowed_filtered_ngrams = narrow_results(word_counts, ngram_counts, filtered_ngrams)
        
        return narrowed_word_counts, narrowed_ngram_counts, narrowed_filtered_ngrams
    
    except Exception as e:
        print(f"Error analyzing text: {e}")
        return None

def check_phrase(phrase="The dog swaggered away."):
    """
    Used to confirm POS tagging for specific phrases. 
    """
    phrase = "The dog swaggered away."
    tokens = word_tokenize(phrase.lower())
    tags = pos_tag(tokens)
    print(tags)


if __name__ == "__main__":
    text = long_text()
    word_counts, ngram_counts, filtered_ngrams = analyze_text(text)
    
    # print filtered ngrams
    for n, counts in filtered_ngrams.items():
        print(f"{n}-grams:")
        for phrase, count in counts.items():
            print(f"{phrase}: {count}")
        print()



    # print(word_counts, '\n\n')
    # print(ngram_counts, '\n\n')
    # print(filtered_ngrams, '\n\n')