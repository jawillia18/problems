def topiclist_1():
    topics = set(["Introduction to Python",
                "Tools of the Trade", 
                "How to make decisions", 
                "How to repeat code", 
                "How to structure data", 
                "Functions", 
                "Modules"])
    
    return topics

def topic_1(sort):

    print('Course Topics:')
    for new_line in sort:
        print("* " + new_line)

def problem():
    problem_list = ["Problem 1", 
                    "Problem 2", 
                    "Problem 3"]

    return problem_list


def adding_problems_2(sort,problems):
    print("Problems:")

    lists = {}
    for i in sort:
        lists[i] = problems
        print("*", i, ": "+ ", ".join(lists[i]))



def status():
    status_list = ["STARTED","GRADED","COMPLETED"]

    return status_list

def student():
    studentName = ("Leah","Zayaan","Imaan")
    return studentName

def keeping_track_3(sort, problems, studentn, statuses):
    print("Student Progress:")
    length = len(studentn)
    for i in range(0,length):
        print(str(i+1)+". "+ studentn[i] , " - " ,sort[i] , " - " ,problems[i] ,"[" + statuses[i] + "]")


def sorting_4(topics):
    topics = sorted(topics)
    return topics

def create_outline():
    """
    TODO: implement your code here
    """
    topics = topiclist_1()
    sort = sorting_4(topics)
    topic_1(sort)
    problems = problem()
    adding_problems_2(sort,problems)
    studentn = student()
    statuses = status()
    keeping_track_3(sort,problems,studentn,statuses)

pass



if __name__ == "__main__":
    create_outline()

    # tuple = ("StudentName","Topics", "problem_list","Status")