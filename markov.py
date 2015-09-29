from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

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

    text_list = text_string.split()

    tup_set = set()
    for i in range(len(text_list)-1):
        tup_set.add((text_list[i], text_list[i+1]))
    
    # Pseudo code:
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

    return chains



def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    first_pair = choice(chains.keys())

    text = first_pair[0] + ' ' + first_pair[1]


    while True:
        try:
            word_to_add = choice(chains.get(first_pair))
            text = text + ' ' + word_to_add
            # Create the next pair for the next iteration of while loop
            first_pair = (first_pair[1], word_to_add)

        # If we reach pair with no words after it, stop
        except IndexError:
            break

    return text


input_path = "zen_of_python.txt"
# Why did the stars in zen of python break this?

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

