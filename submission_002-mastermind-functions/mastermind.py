import random


# TODO: Decompose into functions

def random_code():
    global code
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value

def open_statement():
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    #return 

def player_interact():
    global player
    player = input("Input 4 digit code: ")

def player_progress():   
    global turns
    global correct
    global correct_digits_and_position
    global correct_digits_only 
    correct = False
    turns = 0
    while not correct and turns < 12:
        # answer = input("Input 4 digit code: ") #use def player_interact()
        # everywhere answer is replace it with the variable in player_interact()
        player_interact()
        if len(player) < 4 or len(player) > 4:
            print("Please enter exactly 4 digits.")
            continue
        
        correct_digits_and_position = 0
        correct_digits_only = 0
        for i in range(len(player)):
            if code[i] == int(player[i]):
                correct_digits_and_position += 1
            elif int(player[i]) in code:
                correct_digits_only += 1

        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1

        correct = digits()

    return correct
            
def digits():
    correct = False
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: '+str(12 - turns))
    return correct

def ending():
    print('The code was: '+str(code))

def run_game():
    random_code()
    open_statement()
    correct = player_progress()
    ending()

if __name__ == "__main__":
    run_game()
