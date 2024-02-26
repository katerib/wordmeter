"""
File includes POSPatterns class with CRUD methods to manage custom POS patterns. 

Last updated: 2/25/2024
"""
class POSPatterns:
    """
    A class for managing Part-of-Speech (POS) patterns.

    Attributes:
        patterns (dict): A dictionary storing POS patterns categorized by their length.
            keys: integers representing the length of the POS patterns
            values: dictionaries where:
                keys: tuples of POS tags representing the patterns
                values: descriptions of patterns

    Methods:
        get_patterns(n=None, full_names=False): Retrieve POS patterns.
        get_pos_patterns(n=None): Retrieve all POS patterns abbreviations.
        get_pattern_names(n=None): Retrieve descriptions/names of POS patterns.
        add_pattern(n, pattern, description=""): Add a new pattern with optional description.
        remove_pattern(n, pattern): Remove a pattern.
        update_pattern_name(n, pattern, new_name): Update the description of a pattern.
    """

    def __init__(self):
        """
        Initialize POSPatterns class.
        """
        self.patterns = {
            2: {
                ('JJ', 'NN'): "Adjective-noun",
                ('RB', 'VBD'): "Adverb-verb (past tense)",
                ('NN', 'VBG'): "Noun-gerund",
                ('VBG', 'NN'): "Gerund-noun",
                ('NN', 'NN'): "Noun-noun (compound nouns)",
                ('JJ', 'NNS'): "Adjective-plural noun",
                ('VBD', 'RB'): "Verb (past tense)-adverb",
                ('VB', 'NN'): "Verb-base form-noun",
                ('NNP', 'NNP'): "Proper noun-proper noun",
                ('RB', 'VB'): "Adverb-verb (base form)",
                ('PRP', 'VBP'): "Pronoun-verb (non-3rd person singular present)",
                ('VB', 'RB'): "Verb-base form-adverb",
                ('NN', 'VBD'): "Noun-verb (past tense)",
                ('VBP', 'RB'): "Verb (non-3rd person singular present)-adverb",
                ('RB', 'JJ'): "Adverb-adjective",
                ('VBN', 'RP'): "Verb past participle, particle/adverb",
                ('PRP$', 'NN'): "Possessive pronoun-noun",
                ('VBZ', 'RB'): "Verb (3rd person singular present)-adverb",
                ('VBN', 'IN'): "Verb past participle-preposition",
                ('NN', 'VBZ'): "Noun-verb (3rd person singular present)",
                ('RB', 'VBN'): "Adverb-verb (past participle)",
                ('IN', 'NN'): "Preposition-noun",
                ('NN', 'PRP'): "Noun-pronoun",
                ('JJ', 'VBG'): "Adjective-gerund",
            },
            3: {
                ('DT', 'JJ', 'NN'): "Determiner-adjective-noun",
                ('NN', 'IN', 'NN'): "Noun-preposition-noun",
                ('JJ', 'CC', 'JJ'): "Adjective-conjunction-adjective",
                ('NN', 'VBZ', 'JJ'): "Noun-verb (3rd person singular present)-adjective",
                ('NN', 'JJ'): "Noun-adjective",
                ('IN', 'DT', 'NN'): "Preposition-determiner-noun",
                ('PRP', 'MD', 'VB'): "Pronoun-modal-verb",
                ('VBG', 'IN', 'DT'): "Gerund-preposition-determiner",
                ('DT', 'NN', 'VBZ'): "Determiner-noun-verb (3rd person singular present)",
                ('RB', 'JJ', 'NN'): "Adverb-adjective-noun",
                ('VBD', 'DT', 'NN'): "Verb (past tense)-determiner-noun",
                ('VB', 'PRP$', 'NN'): "Verb-base form-possessive pronoun-noun",
                ('NN', 'CC', 'NN'): "Noun-conjunction-noun",
                ('JJ', 'NN', 'IN'): "Adjective-noun-preposition",
                ('IN', 'JJ', 'NN'): "Preposition-adjective-noun",
                ('DT', 'NN', 'IN'): "Determiner-noun-preposition",
                ('RB', 'VBD', 'IN'): "Adverb-verb (past tense)-preposition",
                ('PRP$', 'JJ', 'NN'): "Possessive pronoun-adjective-noun",
                ('VB', 'DT', 'NN'): "Verb-base form-determiner-noun",
            },
            4: {
                ('DT', 'JJ', 'NN', 'VBZ'): "Determiner-adjective-noun-verb (3rd person singular present)",
                ('RB', 'JJ', 'CC', 'JJ'): "Adverb-adjective-conjunction-adjective",
                ('VBG', 'DT', 'JJ', 'NN'): "Gerund-determiner-adjective-noun",
                ('PRP$', 'NN', 'VBZ', 'JJ'): "Possessive pronoun-noun-verb (3rd person singular present)-adjective",
                ('NNP', 'NNP', 'CC', 'NNP'): "Proper noun-proper noun-conjunction-proper noun",
            },
            5: {
                ('DT', 'JJ', 'NN', 'VBZ', 'JJ'): "Determiner-adjective-noun-verb (3rd person singular present)-adjective",
                ('PRP', 'VBP', 'DT', 'JJ', 'NN'): "Pronoun-verb (non-3rd person singular present)-determiner-adjective-noun",
                ('RB', 'VBG', 'DT', 'JJ', 'NN'): "Adverb-gerund-determiner-adjective-noun",
                ('VBG', 'IN', 'DT', 'NN', 'NN'): "Gerund-preposition-determiner-noun-noun",
                ('NN', 'MD', 'VB', 'DT', 'NN'): "Noun-modal-verb-determiner-noun",
            }
        }

    def get_patterns(self, n=None, full_names=False):
        """
        Retrieve POS patterns (abbreviations with descriptions or just abbreviation format, as specified.)

        Returns:
            If 'n' is specified, return patterns for that length.
            If 'full_names' is True, returns patterns with their descriptions.
        """
        if n:
            patterns = self.patterns.get(n, {})
            if full_names:
                return {pattern: desc for pattern, desc in patterns.items()}
            return {pattern for pattern in patterns.keys()}
        if full_names:
            return {n: {pattern: desc for pattern, desc in p.items()} for n, p in self.patterns.items()}
        return {n: {pattern for pattern in p.keys()} for n, p in self.patterns.items()}

    def get_pos_patterns(self, n=None):
        """
        Retrieve abbreviated POS patterns. 
        
        Returns:
            If n is specified, return patterns for that length.
        """
        if n:
            return self.patterns.get(n, {})
        return self.patterns

    def get_pattern_names(self, n=None):
        """
        Retrieve names of POS patterns. 
        
        Returns: 
            If n is specified, return names for patterns of that length."""
        if n:
            return {pattern: desc for pattern, desc in self.patterns.get(n, {}).items()}
        return {n: {pattern: desc for pattern, desc in p.items()} for n, p in self.patterns.items()}

    def add_pattern(self, n, pattern, description=""):
        """
        Add a new pattern to the specified n-gram patterns, with an optional description.
        """
        if n not in self.patterns:
            self.patterns[n] = {}
        self.patterns[n][pattern] = description

    def remove_pattern(self, n, pattern):
        """
        Remove a pattern from the specified n-gram patterns.
        """
        if n in self.patterns and pattern in self.patterns[n]:
            del self.patterns[n][pattern]
        else:
            print(f"Pattern ({pattern}) not found.")

    def update_pattern_name(self, n, pattern, new_name):
        """
        Update the description/name of a specific pattern.
        """
        if n in self.patterns and pattern in self.patterns[n]:
            self.patterns[n][pattern] = new_name
        else:
            print(f"Pattern ({pattern}) not found.")


if __name__ == "__main__":
    pos_patterns = POSPatterns()
    two_gram_patterns = pos_patterns.get_patterns(2, full_names=True)
    print(two_gram_patterns)
