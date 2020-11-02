import random

def four_digit_code():
    # TODO: Step 1: generate a random 4 digit code
    code = random.sample(range(1,8), 4)
    return code

def usr_prompt():
    usr_input = input("Input 4 digit code: ")
    return list(usr_input)

def input_length(usr_input):
    # len_code = len(code)
    len_input = len(usr_input)
    # while True:
    if len_input == 4:
        # print("Please enter exactly 4 digits.")
        return True
    else:
        return False

def checking_range():
    index = 0
    for i in range(0,len(usr_input)):
        if i != code[index]:
            return usr_input
        else:
            print(usr_input[i])

def run_game():
    code = four_digit_code()
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
   
    usr_input = usr_prompt()
   
    input_length(usr_input)
   
    length = input_length(usr_input)
    while length == False:
        print("Please enter exactly 4 digits.")
        usr_input = usr_prompt()
        length = input_length(usr_input)
    else:
        pass
    """
    TODO: implement Mastermind code here
    """
    pass

if __name__ == "__main__":
    run_game()
            