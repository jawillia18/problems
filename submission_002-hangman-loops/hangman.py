import random
import sys

def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    word.lower()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    rand_let = random.randint(0,len(word) -1)
    chosen_let = word[rand_let]
    clue_letter = "_"*len(word)
    new_word = clue_letter[ :rand_let]+ chosen_let+ clue_letter[rand_let+1: ]
    return new_word

# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    if char in original_word and char not in answer_word:
        return True
    else:
        return False

# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    guesses = "_"*len(original_word)
    for index, letter in enumerate(original_word):
        if letter == char:
            if index != len(original_word):
                answer_word= answer_word[:index] + letter + answer_word[index+1:]
            else:
                answer_word = answer_word[:-1] + letter
    return answer_word


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    stages = [
        """
/----
|   0
|  /|\\
|   |
|  / \\
_______""",
"""
/----
|   0
|  /|\\
|   |
|
_______""",
"""
/----
|   0
|  /|\\
|
|
_______""",
"""
/----
|   0
|
|
|
_______""",
"""
/----
|
|
|
|
_______""",
    ] 
    print (stages[number_guesses])



# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer): 
    number_guesses = 5              
    print("Guess the word: "+ answer)    
                                                                                                                              
    while True:
        guess = get_user_input().lower()
        if guess == "exit" or guess == "quit":
            print("Bye!")
            break
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
            print(answer)
        else:
            number_guesses -= 1
            do_wrong_answer(answer, number_guesses)
        if answer == word:
            break
        if number_guesses == 0:
            print("Sorry, you are out of guesses. The word was: " + word)
            break





# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":

    if len(sys.argv) == 1:
        words_file = ask_file_name()
    else:
        words_file = sys.argv[1]
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

