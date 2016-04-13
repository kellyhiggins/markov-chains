from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read()

    return text_string
    # "This should be a variable that contains your file text as one long string"


def make_chains(text_string):
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
    for i in range(len(words)-2):
        # iterating over our list of words, determining word1 and word2 based on their index
        #taking the next word in our list and making it the value for our tuple key
        # check if key in dictionary
        # if not add it to dictionary, and add value

        if (words[i], words[i+1]) in chains:
            #key exists and I am appending the list of values
            chains[(words[i], words[i+1])].append(words[i+2])
        else:
           chains[(words[i], words[i+1])] = [words[i+2]]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    print "Dictionary: ", chains
    word_list = []
    #get the first random key from the dictionary
    rand_tuple = choice(chains.keys())
    word1 = rand_tuple[0]
    word2 = rand_tuple[1]

    # make tuple into list
    word_list.append(word1)
    word_list.append(word2)
    key = (word1, word2)
    # print "created key from the return tuple: ", key
    # print "Word List:" ,word_list
    

    while True:
    # iterate over dictionary and append to list
        possible_next_words = chains.get(key) 
        # print "the key: ", key   
        # print "Possible Next Words: ",possible_next_words
        # print "***********************************"
        if possible_next_words: 
            value = choice(chains[key])
            print "Value: ", value
            # append to final list
            word_list.append(value)  
        # word swapping (reassign key)
            key = (word2, value)
            print "key: ",key
            print "word_list: ", word_list
        elif possible_next_words == None:
            break

    ' '.join(word_list)

    return

# link is a key from our dictionary and a random word from the list
# put that link into a container (concatenating into string)
# once we have first link, can add another to it,
# can keep adding more in repetetive process
    # make a new key out of second word in first key, and random value
    # look up new key in dictionary, pull a new random value
    # keep doing that until Key Error
    # word2 becomes word1
    # use value will become word2

# UNTIL we hit sam i, which can only end in am.
    #text = ""

        # concatenate list into string

    


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
