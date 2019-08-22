"""
Author: Aidan Jude
Date: 08/21/2019

Description: 
    This program fetches random quotes from favorite authors (listed below in a set) and changes the adjectives
    of the quote to a nearby synonym utilizing the machine learning techniques of NLP.

Logic Flow: 
    1. Fetch random quote from favorite author (selected at random) by scraping Brainy Quote
    2. Utilize TextBlob NLP library to assign POS tags to the words from the quote fetched
    3. Identify synonyms for the adjectives of the quote
    4. Replace the original quote with the newly selected adjectives

Library Documentation: 
    TextBlob: https://textblob.readthedocs.io/en/dev/

POS Tags:
    CC coordinating conjunction
    CD cardinal digit
    DT determiner
    EX existential there (like: “there is” … think of it like “there exists”)
    FW foreign word
    IN preposition/subordinating conjunction
    JJ adjective ‘big’
    JJR adjective, comparative ‘bigger’
    JJS adjective, superlative ‘biggest’
    LS list marker 1)
    MD modal could, will
    NN noun, singular ‘desk’
    NNS noun plural ‘desks’
    NNP proper noun, singular ‘Harrison’
    NNPS proper noun, plural ‘Americans’
    PDT predeterminer ‘all the kids’
    POS possessive ending parent’s
    PRP personal pronoun I, he, she
    PRP$ possessive pronoun my, his, hers
    RB adverb very, silently,
    RBR adverb, comparative better
    RBS adverb, superlative best
    RP particle give up
    TO, to go ‘to’ the store.
    UH interjection, errrrrrrrm
    VB verb, base form take
    VBD verb, past tense took
    VBG verb, gerund/present participle taking
    VBN verb, past participle taken
    VBP verb, sing. present, non-3d take
    VBZ verb, 3rd person sing. present takes
    WDT wh-determiner which
    WP wh-pronoun who, what
    WP$ possessive wh-pronoun whose
    WRB wh-abverb where, when
"""

from QuoteFetch import *
from textblob import TextBlob
from textblob import Word

def main():
    favorite_authors = ['F Scott Fitzgerald', 'Thomas Wolfe', 'Cormac McCarthy', 'John Keats',
                            'T S Eliot', 'John Steinbeck', 'W B Yeats', 'Ernest Hemingway',
                            'Rupert Brooke', 'John Milton', 'C S Lewis', 'Friedrich Nietzsche',
                            'Percy Shelley', 'Lord Byron']

    y = random.choice(range(0, 12, 1))
    quote = get_random_quote(favorite_authors[y]) + ' - ' + favorite_authors[y]

    #print original quote
    print("------------------------------------------------")
    print("Original Quote:")
    print(quote)
    print('\n')

    #find the adjectives and replace them with synonyms 
    blob = TextBlob(quote)
    print("Adjectives:")
    for word in blob.pos_tags:
        if word[1] in ['JJ', 'JJR', 'JJS']:
            for synset in word[0].synsets:
                #if the synonym is not the same word
                if synset.lemmas()[0].name() != word[0]:
                    print(word[0] + ' ' + word[1] + ' ------- ' + synset.lemmas()[0].name())
                    quote = quote.replace(word[0], synset.lemmas()[0].name())
                    break

    print("\n")
    print("Final Quote:")
    print(quote)
    print("------------------------------------------------")

if __name__ == "__main__":
    main()