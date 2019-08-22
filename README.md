# Quotable_NLP_Synset

This program (written in python) fetches random quotes from favorite authors and changes the adjectives of the quote to a nearby synonym utilizing the machine learning techniques of NLP.

Logic Flow: 
    1. Fetch random quote from favorite author (selected at random) by scraping Brainy Quote
    2. Utilize TextBlob NLP library to assign POS tags to the words from the quote fetched
    3. Identify synonyms for the adjectives of the quote
    4. Replace the original quote with the newly selected adjectives

Library Documentation: 
    TextBlob: https://textblob.readthedocs.io/en/dev/
