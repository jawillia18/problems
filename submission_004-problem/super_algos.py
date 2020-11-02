element = [3,4,7,2,6]
length = len(element)-1
element2 = [3,4,7,2,6]

def find_min(element):
    """TODO: complete for Step 1"""
    if len(element) == 0:
        return -1
    elif type(element[0]) != type(2):
        return -1
    if len(element) == 1:
        return element[0]
    elif element[0] < element[1]:
        element.pop(1)
    else: 
        element.pop(0)
        return element[0]
    return find_min(element)
    """returns -1 if the list is empty or if an element in the list 
    is not a integer
    the .pop removes an element in the list if it does not meet the conditions as it recurses 
    until theres only one element left and it print that element"""
    

def sum_all(element2):
    """TODO: complete for Step 2"""
    
    if len(element2) == 0:
         return -1
    elif type(element2[0]) != type(2):
        return -1
    elif (len(element2) == 1):
        return element2[0]
    return element2.pop() + sum_all(element2)
    """if the list is empty or not an integer it returns -1
    else .pop() removes the last element of a list unless stated otherwise and when 
    its done popping it recurses and adds all the numbers"""


# def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    # pass
print(find_min(element))
print(sum_all(element2))
