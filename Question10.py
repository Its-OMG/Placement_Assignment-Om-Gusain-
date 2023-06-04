# To do this question, we will have to use Natural Language Toolkit or nltk.
# This library will help us categorize each word into nouns, pronouns, verbs and adjectives
# Note: I had to read nltk documentation understand the usage of nltk methods 

import nltk 

#let's make a function first which will take a string as argument
def count_english(string):
    # Now, the string will be tokenized to individual words 
    text_token = nltk.word_tokenize(string)

    # Each token created from the string will be POS tagged
    tags = nltk.pos_tag(text_token)

    # Let's create the dict now
    words_dict = {
        'Nouns': 0,
        'Pronouns': 0,
        'Verbs': 0,
        'Adjectives': 0
    }

    # Now, we will iteratively check the POS tagged word and Increment the values of keys in the dict accordingly
    for word, pos in tags:
        if pos.startswith("NN"):
            words_dict['Nouns']+=1
        if pos.startswith("PRP"):
            words_dict['Pronouns']+=1
        if pos.startswith("VB"):
            words_dict['Verbs']+=1
        if pos.startswith("JJ"):
            words_dict['Adjectives']+=1
    

    # The dictionary will be returned
    return words_dict


a = "Hello There! How are you? I am doing fine, Thank you!"                         # Testcase 1
b = "I want to play cricket today! The weather is really beautiful for that."       # Testcase 2
c = "You play piano very gracefully! I want to learn it too!"                       # Testcase 3
print(f"Sentence One Word Counts: {count_english(a)}\n")
print(f"Sentence two Word Counts: {count_english(b)}\n")
print(f"Sentence Three Word Counts: {count_english(c)}\n")
