

#TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shapes = input("Shape?: ").lower()
    if shapes == "pyramid":
        return "pyramid"
    elif shapes == "square":
        return "square"
    elif shapes == "triangle":
        return "triangle"
    elif shapes == "rectangle":
        return "rectangle"
    else:
        return get_shape()


# TODO: Step 1 - get height (it must be int!)
def get_height():
    try:
        height = int(input("Height?: "))
        return height
    except:
        return get_height()


# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == True:
        for row in range(height):
            for col in range(height-row-1):
                print(" ", end="")
            for col in range(2*row+1):
                if col == 0 or col ==2*row or row == height -1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    else:
        for row in range(0, height):
            for col in range(0, height - 1 - row):
                print(" ", end="")
            for stars in range (0, 2* row + 1):
                print("*", end="")
            print()
        # print("pyramid")



# TODO: Step 3
def draw_square(height, outline):
    if outline == True:
         for row in range(1, height+1):
            if row == 1 or row== height:
                print("*" *height)
            else:
                print("*" + " "*(height- 2) + "*")
    else:
        for i in range(0,height):
            for j in range(0,height):
                print("*",end="")
            print()
    #print("square")


# TODO: Step 4
def draw_triangle(height, outline):
    if outline == True:
        for row in range(height):
            for col in range(row+1):
                if col==0 or row==(height-1) or row==col:
                    print("*",end="")
                else:
                    print(end=" ")
            print()
    else:
        for i in range(0,height):
            for j in range(0,height-1):
                print(end="")
            for j in range(0,i+1):
                print("*",end="")
            print()
    #print("triangle")


def draw_rectangle(height, outline):
    if outline == True:
        for rows in range(height):
            for col in range(height+2):
                if rows==0 or rows==height-1 or col== 0 or col == (height+2)-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print() 
    else:
        for row in range(height):
            print("*"*(row+1)+"*"*(height-row+1))

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height,outline)
    elif shape == "square":
        draw_square(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)
    elif shape == "rectangle":
        draw_rectangle(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline only (y/n): ").lower()
    if outline == "y" or outline == "Y":
        return True
    elif outline == "n" or outline == "N":
        return False
    else:
        return get_outline()

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

