import os
import sys

from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read()

    return text_string
    # "This should be a variable that contains your file text as one long string"


def make_chains(text_string, n_gram=2):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    #intializing our dictionary
    chains = {}
            # key = (words[i], words[i+1])
            # value = (words[i+2])
    
    #creating a list of our words
    words = text_string.split()

    #we are going to make a tuple of the first two words based on the index of our words
    for i in range(len(words)-n_gram):
        # iterating over our list of words, determining word1 and word2 based on their index
        #taking the next word in our list and making it the value for our tuple key
        # check if key in dictionary
        # if not add it to dictionary, and add value
# create for loop with n_gram
        key = []

        # make into a list, then convert to tuple
        for e in range(n_gram -1):
            key.append(words[i+e])
        key = (key)
        try: 
            chains[key].append(words[i+n_gram])
        except KeyError:
            chains[key] = [words[i+n_gram]]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    word_list = []
    #get the first random key from the dictionary
    key = choice(chains.keys())
    
    word_list.append(key[0])
    word_list.append(key[1])

    # print "created key from the return tuple: ", key
    # print "Word List:" ,word_list

    while True:
    # iterate over dictionary and append to list
        if chains.get(key) == None: 
            break
        else:     
            value = choice(chains[key])
            # append to final list
            word_list.append(value)  
            # word swapping (reassign key)
            key = (key[1], value)

    return ' '.join(word_list)
###################################################################
    


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
