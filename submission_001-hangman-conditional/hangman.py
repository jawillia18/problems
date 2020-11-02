import random


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()
    """reads the contents of the file chosen"""

def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index]
    return word
    """choosing a random word from a list  """

def select_random_letter_from(word):
    random_index = random.randint(0, len(word) - 1)
    letter = word[random_index]
    print('Guess the word: ' + word[:random_index] + "_" + word[random_index+1:])
    return letter, random_index
    """choosing a random letter in the random word and replacing it with a underscore
    word[:random_index] print the letters after the random position """

def get_user_input():
    guess = input('Guess the missing letter: ')
    return guess
    """asking the user to guess the word"""

def show_answer(answer, selected_word, missing_letter_index):
    """
    TODO Step 1 - Show better results messages
    """
    
    print("The word was: " + selected_word)
    if answer in selected_word:
        print("Well done! You are awesome! ")
    else:
         print("Wrong! Do better next time. ")
    pass
"""prints the whole word and depending on whether you got it right or nor it prints the results message"""

# TODO: Step 2
def ask_file_name():
    """
    TODO Step 2 - Update to prompt user for filename to use for words
    """
    usrfile = input('Words file? [leave empty to use short_words.txt] : ')
    if(usrfile == ""):
        return "short_words.txt"
    else: return usrfile 
"""option to choose a file or just use the default file"""

def run_game(file_name):
    """
    You can leave this code as is, and only implemented above where the code comments prompt you.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    missing_letter, letter_index = select_random_letter_from(word)
    answer = get_user_input()
    show_answer(answer, word, letter_index)


if __name__ == "__main__":
    words_file = ask_file_name()
    run_game(words_file)

