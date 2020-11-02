import functools

new_list = []
text = 'These are indeed interesting, an obvious understatement, times. What say you?'

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    word = split(" ,;?.",text)
    filter_word = list(filter(lambda x: x != "", word))
    lower_word = list(map(lambda x : x.lower(),filter_word))
    return lower_word
    """this seperates the words into a list and removes all the spaces and makes it 
    all lowercase"""


def words_longer_than(length,text):
    word = split(" ,;?.",text)
    filter_word = list(filter(lambda x: x != "" and len(x) > length, word))
    lower_word = list(map(lambda x : x.lower(),filter_word))
    return lower_word
    """returns all the words with a specific number of letters only in a list"""

def words_lengths_map(text):
    word = split(" ,;?.",text)
    filter_word = list(filter(lambda x: x != "", word))
    lower_word = list(map(lambda x : x.lower(),filter_word))
    key_words = [len(x) for x in lower_word]

    words_length = {x:key_words.count(x) for x in sorted(key_words)}
    return words_length
    """how many words occur of each length."""



def letters_count_map(text):
    index_words = list(text.lower())
    alpha = {"a","b","c","d","e","f","g","h",
        "i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
    words_length = {x:index_words.count(x) for x in sorted(alpha)}
    return words_length
    """returns a disctionry showing how many times a certain letter occurs"""

def most_used_character(text):
    words_length = letters_count_map(text)
    values = list(map(lambda i: words_length[i],words_length))
    max_num = functools.reduce(lambda x,y: x if x > y else y, values)
    for key , value in words_length.items():
        if max_num == value:
            return key
    """return the letter that occurs the most times in the string"""
# print(convert_to_word_list(text))
# print(words_longer_than(10,text))
# print(words_lengths_map(text))
# print(letters_count_map(text))
# print(most_used_character(text))