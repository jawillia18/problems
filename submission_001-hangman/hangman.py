#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    F = open(file_name)
    lists = F.readlines()
    return lists


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    str_lenghth = len(words) - 1
    randomwords = random.randint(0,str_lenghth)
    word = words[randomwords]
    swords = word.split()
    letter = random.choice(swords)
    strg =len(letter) - 1
    index = random.randint(0,strg)
    print('Guess the word: ' + letter[0:index] + '_' + letter[index + 1:strg + 1])
    
    return word



def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    fill = input("Guess the missing letter: ")
    return fill


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

