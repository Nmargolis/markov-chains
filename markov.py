from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_object = open(file_path)
    text = file_object.read()
    text = text.strip()

    return text


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # your code goes here
    text_list = text_string.split()

    tup_set = set()
    for i in range(len(text_list)-1):
        tup_set.add((text_list[i], text_list[i+1]))
    
    # loop through set of tuples
    #     key = tup
    #     value = []
    #     loop through text_list using i and range
    #         if word[i] == tup0
    #             if word[i+1] == tup1
    #                 append word[i+2] to valuelist
    #     add key and value to chains

    for tup in tup_set:
        key = tup
        value = []
        for i in range(len(text_list)-2):
            if text_list[i] == tup[0]:
                if text_list[i+1] == tup[1]:
                    value.append(text_list[i+2])
        chains[key] = value

    # print chains
    return chains



def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

# pull out random key from dictionary
# unpack tuple as 1st & second word and append to text string/or list

# loop through dictionary 
#     find that tuple to find
#         pick a random word from the value with that key and call it next word
#         append the next word to text string
#     next tuple = second word, next word
#     tuple to find = next tupple


    first_pair = choice(chains.keys())
    # print first_pair
    text = first_pair[0] + ' ' + first_pair[1]
    # print text

    # print "first_pair is ", first_pair

    while True:
        # if chains.get(first_pair, 0) == 0:
        #     break
        # else:
        #     for key in chains:
        #         # print "Key is ", key
        #         if key == first_pair:
        try:
            word_to_add = choice(chains.get(first_pair))
            # print chains.get(key)
            # print key
            # print word_to_add
            text = text + ' ' + word_to_add
            first_pair = (first_pair[1], word_to_add)
            # print "new first_pair is ", first_pair
        except IndexError:
            break

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# print "%r" % input_text

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

