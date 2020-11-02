lists = ["jay","cal","leah"]

def input_jay():
    
    name = input("name the robot?")
    return name

def new_list_2(new_list = []):

    for name in lists:
        name = input_jay()
        new_list.append(name)
        print(new_list)
        return new_list

def input_name():
    # input_jay()
    new_list_2(new_list=[])

if __name__ == "__main__":
    input_name()