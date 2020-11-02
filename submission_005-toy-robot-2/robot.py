position = 0
x = 0
y = 0
def robot_name():
    name = input("What do you want to name your robot? ")
    if len(name) == 0:
        return robot_name()
    else:
        return name
    """Function to name robot and repeats question if there is no response"""


def robot_response(name):
    print(name + ": " + "Hello kiddo!")
    return name


def action_prompt(name, command):
    action = ''
    action = input(name + ": " + "What must I do next? ")
    # action = action.lower()
    sep = action.split(' ')
    if len(action) == 0:
        print(name + ": " + "Sorry I did not understand")
        return action_prompt(name, command)
    elif sep[0].upper() not in command:
        print(name + ": " + "Sorry, I did not understand " + repr(action)+ ".")
        return action_prompt(name, command)
    return action.lower()
    """this function contains a input that asks the player 
    for a action and if the action does not correspond with any of the commands provided
    or the input is empty it prints out a message that states the robot does not understand"""


def commands():
    command = ["OFF",
                "HELP",
                "BACK",
                "RIGHT",
                "LEFT",
                "SPRINT",
                "FORWARD"]
    return command


def split(action,command,name):

    if action.upper() in command:
        num = 0
    else:
        (action,num) = action.split(' ')
        num = int(num)
    return action, num
    """splits the action which is the answer that the player provided 
    into two the command and the number that we later use to determine the 
    co-ordinates of the robot"""

def descriptions():
    descr = [" - Shut down robot",
            "- provide information about commands",
            "- Moves the robot backward a certain amount",
            "- Turns 90 degrees to the right",
            "- Turns 90 degrees to the left",
            "- Sprint gives it a short burst of speed and some extra distance",
            "- Moves robot forward a certain amount"]
    return descr


def help_functions(descr,command):

    length = len(command)
    print("I can understand these commands:")
    for x in range(0,length):
        print(command[x]+ "" , descr[x])
    return command,descr
    """this function joins the two lists (the command list)(the description list) to create 
    the help function the description list describes
    the command you choosing to use"""


def turn_statement(name,action):
    print(" >",name,"turned",action+".")


def moving_forward(action,name,command,num):
    global position,x,y
    num = int(num)
    if position == 0:
        y = y + num
    elif position == 90:
        x = x + num
    elif position == 180:
        y = y - num
    elif position == 270:
        x = x - num
    if x > -101 and x < 101 and y > -201 and y < 201:
        coord = (x,y)
        new_co = str(coord).replace(" ","")
        new_co = str(new_co)
        print(" >",name,"moved",action,"by",num,"steps.")
        print(" >",name, "now at position",new_co+".")
        return x,y
        """this statement gives a area limit to the robot to it 
        cannot exceed a certain number in retrospec cannot exceed the border"""
    else:
        print(name + ": Sorry, I cannot go outside my safe zone.")
        x = 0
        y = 0
        coord = (x,y)
        new_co = str(coord).replace(" ","")
        new_co = str(new_co)
        print(" >",name, "now at position",new_co+".")
        return x,y
        """this determines whether the num will change the x or y co-ordinate and how, 
        the forward function adds so if the "robot" is at position 90 it affects the x co-ordinate"""
        """this is to remove the spaces in the co-ordinates"""
        """this is when the area limit has been exceeded it returns the 
        robot back to square one and resets the co-ordinates to the origin point (0,0)"""


def moving_back(action,name,command,num):
    global position,x,y
    num = int(num)

    if position == 0:
        y = y - num
    elif position == 90:
        x = x - num
    elif position == 180:
        y = y + num
    elif position == 270:
        x = x + num
    """this function essentially does the same thing as forward so depending 
    on the position which is determined when you turn left/right you are changing either 
    the x co-ord or the y co-ord and the back function subtracts rather then add """
    if x > -101 and x < 101 and y > -201 and y < 201:
        coord = (x,y)
        new_co = str(coord).replace(" ","")
        new_co = str(new_co)
        print(" >",name,"moved",action,"by",num,"steps.")
        print(" >",name, "now at position",new_co+".")
        return x,y
    else:
        print(name + ": " + "Sorry, I cannot go outside my safe zone.")
        x = 0
        y = 0
        coord = (x,y)
        new_co = str(coord).replace(" ","")
        new_co = str(new_co)
        print(" >",name, "now at position",new_co+".")
        return x,y
        """this is to remove the spaces in the co-ordinates"""
        """this is when the area limit has been exceeded it returns the 
        robot back to square one and resets the co-ordinates to the origin point (0,0)"""


def turn_right(num,name,command,action):
    global position,x,y
    coord = (x,y)
    new_co = str(coord).replace(" ","")
    new_co = str(new_co)
    print(" >",name, "now at position",new_co+".")
    
    if position == 0:
        position = 90
    elif position == 90:
        position = 180
    elif position == 180:
        position = 270
    elif position == 270:
        position = 0
    return x,y
    """this function changes the position of the robot and determines which axis the robot
    will be moving on when you type right its turning clockwise """

    
def turn_left(num,name,command,action):
    global position,x,y
    coord = (x,y)
    new_co = str(coord).replace(" ","")
    new_co = str(new_co)
    print(" >",name, "now at position",new_co+".")
    
    if position == 0:
        position = 270
    elif position == 90:
        position = 0
    elif position == 180:
        position = 90
    elif position == 270:
        position = 180
    return x,y
    """this functions serves the same purpose as the turn right function 
    it changes the position and turns anti-clockwise"""


def robot_sprint(num,name):

    if num > 0:
        print(" >", name,"moved forward by",num,"steps.")
        return num + robot_sprint((num)-1,name)
    else:
        return num
        """this function is recursive so the number the player entered
        keeps getting subtracted by one everytime the function recurses and prints out the
        statement until it reaches 0 and it breaks out the recursion"""


def sprint_coordinates(num,name):
    global position,x,y
    num = robot_sprint(num,name)

    if position == 0:
        y = y + num 
    elif position == 90:
        x = x + num
    elif position == 180:
        y = y - num
    elif position == 270:
        x = x - num


    if x > -101 and x < 101 and y > -201 and y < 201:
        coord = (x,y)
        new_co = str(coord).replace(" ","")
        new_co = str(new_co)
        print(" >",name, "now at position",new_co+".")
        return x,y
    else:
        print(name + ": " + "Sorry, I cannot go outside my safe zone.")
        x = 0
        y = 0
        coord = (x,y)
        new_co = str(coord).replace(" ","")
        new_co = str(new_co)
        print(" >",name, "now at position",new_co+".")
        return x,y
        """a area limit is set and prints the necessary statement with the current co-ords,
        when the area limit has been exceeded it returns the 
        robot back to square one and resets the co-ordinates to the origin point (0,0)
        and prints the necessary statement"""
    

def set_commands(action,name,descr,command):

    while True:
        action,num = split(action,command,name)
        if action == "off":
            print(name + ":"+ " Shutting down..")
            break
        elif action == "help":
            help_functions(descr,command)
        elif action == 'forward':
            moving_forward(action,name,command,num)
        elif action == "back":
            moving_back(action,name,command,num)
        elif action == "right":
            turn_statement(name,action)
            turn_right(num,name,command,action)
        elif action == 'left':
            turn_statement(name,action)
            turn_left(num,name,command,action)
        elif action == "sprint":
            sprint_coordinates(num,name)
        action = action_prompt(name, command)    
        """this is the main function where everything is in a loop so it runs continuously until you type off
        and it breaks out"""
def robot_start():
    global x,y,position
    x = 0
    y = 0
    position = 0
    name = robot_name()
    name = robot_response(name)
    command = commands()
    action = action_prompt(name, command)
    descr = descriptions()
    set_commands(action,name,descr,command)

    """This is the entry function, do not change"""
    pass
if __name__ == "__main__":
    robot_start()
