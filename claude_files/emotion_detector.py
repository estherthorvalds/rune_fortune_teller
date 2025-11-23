"""
Emotion Detector for Rune Fortune Teller by Claude's Sonnet 4.5
Takes preprocessed lemmas (from your SpaCy preprocessing) and detects emotional category.
"""

from .category_analyzer import analyze_category


def detect_emotion_from_csv(csv_filepath):
    """
    Read lemmas from a CSV file (output from preprocessing-5.py) and detect category.
    Expects CSV format: wordform, POS-tag, lemma
    
    Parameters:
    -----------
    csv_filepath : str
        Path to CSV file with format: word\ttag\tlemma
        
    Returns:
    --------
    str
        The category: "LOVE", "HEALTH", or "FINANCE"
    """
    lemmas = []
    
    with open(csv_filepath, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                lemma = parts[2]  # Third column is lemma
                lemmas.append(lemma)
    
    category = analyze_category(lemmas)
    return category


def detect_emotion_from_lemmas(lemmas):
    """
    Detect emotional category from a list of lemmas.
    
    Parameters:
    -----------
    lemmas : list
        List of lemmatized words
        
    Returns:
    --------
    str
        The category: "LOVE", "HEALTH", or "FINANCE"
    """
    category = analyze_category(lemmas)
    return category


# Testing
if __name__ == "__main__":
    # Test with sample lemmas
    test_lemmas = ["relationship", "boyfriend", "love", "fight", "miss", "heart"]
    
    print("Testing emotion_detector.py")
    print("=" * 60)
    print(f"Test lemmas: {test_lemmas}")
    
    category = detect_emotion_from_lemmas(test_lemmas)
    print(f"Detected category: {category}")
    print()
    print("✓ Ready to use in your Rune Fortune Teller program!")
