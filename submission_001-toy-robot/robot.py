

def move(): #instructions(): #   because im giving instructions on which direction whoever needs to move
# TODO: Decompose into functions
    move_square()
    move_rectangle()
    move_circle()
    square_dancing()
    crop_circle()

def move_square():
    size = 10
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")

def move_rectangle():
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


def move_circle():
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")

def square_dancing():
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a square of size 20")
        for j in range(4):
            size = 20
            degrees = 90
            print("* Move Forward " + str(size))
            print("* Turn Right " + str(degrees) + " degrees")

def crop_circle():
    print("Crop circles - 4 circles")
    for i in range(4):
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a circle")
        for k in range(360):
            length = 1
            degrees = 1
            print("* Move Forward " + str(length))
            print("* Turn Right " + str(degrees) + " degrees")


def robot_start():
    move()


if __name__ == "__main__":
    robot_start()