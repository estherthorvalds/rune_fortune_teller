"""
Category Analyzer for Rune Fortune Teller by Claude's Sonnet 4.5
Takes lemmatized text and determines which emotional category 
(LOVE, HEALTH, FINANCE) has the most matches.
"""

from .emotion_words import LOVE, HEALTH, FINANCE


def analyze_category(lemmas):
    """
    Analyzes a list of lemmas and determines which category is most prominent.
    
    Parameters:
    -----------
    lemmas : list
        A list of lemmatized words from the user's input text
        
    Returns:
    --------
    str
        The winning category: "LOVE", "HEALTH", or "FINANCE"
        If there's a tie, returns the first category in order of priority
    """
    # Convert all lemmas to lowercase for comparison
    lemmas_lower = [lemma.lower() for lemma in lemmas]
    
    # Count matches for each category
    love_count = sum(1 for lemma in lemmas_lower if lemma in LOVE)
    health_count = sum(1 for lemma in lemmas_lower if lemma in HEALTH)
    finance_count = sum(1 for lemma in lemmas_lower if lemma in FINANCE)
    
    # Determine winner
    if love_count > health_count and love_count > finance_count:
        return "LOVE"
    elif health_count > love_count and health_count > finance_count:
        return "HEALTH"
    elif finance_count > love_count and finance_count > health_count:
        return "FINANCE"
    else:
        # Handle ties - return the category with highest priority
        # Priority order: LOVE > HEALTH > FINANCE
        max_count = max(love_count, health_count, finance_count)
        if love_count == max_count:
            return "LOVE"
        elif health_count == max_count:
            return "HEALTH"
        else:
            return "FINANCE"


def analyze_category_with_counts(lemmas):
    """
    Analyzes lemmas and returns both the winning category and the counts.
    Useful for debugging or displaying statistics to the user.
    
    Parameters:
    -----------
    lemmas : list
        A list of lemmatized words from the user's input text
        
    Returns:
    --------
    tuple
        (winning_category, love_count, health_count, finance_count)
    """
    # Convert all lemmas to lowercase for comparison
    lemmas_lower = [lemma.lower() for lemma in lemmas]
    
    love_count = sum(1 for lemma in lemmas_lower if lemma in LOVE)
    health_count = sum(1 for lemma in lemmas_lower if lemma in HEALTH)
    finance_count = sum(1 for lemma in lemmas_lower if lemma in FINANCE)
    
    # Determine winner using the same logic
    if love_count > health_count and love_count > finance_count:
        winner = "LOVE"
    elif health_count > love_count and health_count > finance_count:
        winner = "HEALTH"
    elif finance_count > love_count and finance_count > health_count:
        winner = "FINANCE"
    else:
        max_count = max(love_count, health_count, finance_count)
        if love_count == max_count:
            winner = "LOVE"
        elif health_count == max_count:
            winner = "HEALTH"
        else:
            winner = "FINANCE"
    
    return winner, love_count, health_count, finance_count


def get_matching_words(lemmas, category):
    """
    Returns which specific words from the text matched a given category.
    Useful for understanding why a text was categorized a certain way.
    
    Parameters:
    -----------
    lemmas : list
        A list of lemmatized words from the user's input text
    category : str
        The category to check: "LOVE", "HEALTH", or "FINANCE"
        
    Returns:
    --------
    list
        List of lemmas that matched the category (may contain duplicates)
    """
    category_upper = category.upper()
    
    # Convert all lemmas to lowercase for comparison
    lemmas_lower = [lemma.lower() for lemma in lemmas]
    
    if category_upper == "LOVE":
        return [lemma for lemma in lemmas_lower if lemma in LOVE]
    elif category_upper == "HEALTH":
        return [lemma for lemma in lemmas_lower if lemma in HEALTH]
    elif category_upper == "FINANCE":
        return [lemma for lemma in lemmas_lower if lemma in FINANCE]
    else:
        raise ValueError(f"Invalid category: {category}. Must be 'LOVE', 'HEALTH', or 'FINANCE'")


# Example usage and testing
if __name__ == "__main__":
    # Test with sample lemmatized text
    test_lemmas = [
        "love", "relationship", "partner", "heart", "feel", "emotion",
        "money", "pay", "health", "doctor", "kiss", "romantic"
    ]
    
    print("Testing category_analyzer.py")
    print("=" * 50)
    print(f"Test lemmas: {test_lemmas}")
    print()
    
    # Test basic function
    category = analyze_category(test_lemmas)
    print(f"Winning category: {category}")
    print()
    
    # Test function with counts
    winner, love, health, finance = analyze_category_with_counts(test_lemmas)
    print(f"Detailed results:")
    print(f"  LOVE: {love} matches")
    print(f"  HEALTH: {health} matches")
    print(f"  FINANCE: {finance} matches")
    print(f"  Winner: {winner}")
    print()
    
    # Test get_matching_words
    love_words = get_matching_words(test_lemmas, "LOVE")
    print(f"Words that matched LOVE: {love_words}")
