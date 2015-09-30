from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_object = open(file_path)
    text = file_object.read()
    text = text.strip()

    return text


def make_chains(text_string, n): # second argument will be n
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    text_list = text_string.split()

    tup_set = set()

    # Loop over text_list n-1 times to populate tup_set with tuples of n length
    for i in range(len(text_list)-(n-1)):
        # Add a tuple comprised of a slice of text_list that is n items long to the tup_set
        tup_set.add(tuple(text_list[i:i+n]))


    # hello there joel hello there cynthia hello there katie
    # (hello, there), (there, joel)



    # (hello, there) = joel
    # (there, joel) = hello

    # Pseudo code:
    # loop through set of tuples
    #     key = tup
    #     value = []
    #     loop through text_list using i and range
    #         if word[i] == tup0
    #             if word[i+1] == tup1
    #                 append word[i+2] to valuelist
    #     add key and value to chains

    # Populate the chains dictionary
    for tup in tup_set:
        key = tup
        value = []
        # counter keeps track of how far to slice the text_list
        counter = n
        
        for index_of_word in range(len(text_list)-n):
            # if a slice of the list from index to counter (converted to a tuple)
            #is equal to tup
            if tuple(text_list[index_of_word:counter]) == tup:
                #Add the next word after the tuple to the value associated with tup
                value.append(text_list[index_of_word+n])
              
            counter += 1

        chains[key] = value

    return chains



def make_text(chains, n):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    first_ngram = choice(chains.keys())

    # print 'first ngram: ', first_ngram

    for i in range(n):
        text = text + ' ' + first_ngram[i]
    # text = text + 'FIRST ONE'  

    while True:
        try:
            # Choose and add the next word
            word_to_add = choice(chains.get(first_ngram))
            text = text + ' ' + word_to_add #+ '!!!!'
            # Create the next pair for the next iteration of while loop
            # print "slice: ", first_ngram[1:n]

            # Create the next ngram from the last two in first_ngram + next word
            ngram_list = list(first_ngram[1:n])
            ngram_list.append(word_to_add)

            first_ngram = tuple(ngram_list)
            # print "new ngram: ", first_ngram


        # If we reach pair with no words after it, stop
        except IndexError:
            break

    return text


input_path = sys.argv[1]
# Why did the stars in zen of python break this?

# n = sys.argv[2]
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 4)

# Produce random text
random_text = make_text(chains, 4)

print random_text

