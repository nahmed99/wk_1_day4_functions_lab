tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]




# 1. Print a list of uncompleted tasks
# 2. Print a list of completed tasks
def get_uncompleted_tasks(list, bool_flag):
    uncompleted_tasks = []
    for task in list:
        #if task["completed"] == False:
        if task["completed"] == bool_flag:
            uncompleted_tasks.append(task)

    return uncompleted_tasks


# 3.
def get_descriptions(list):
    task_description = []
    for task in list:
        task_description.append(task["description"])

    return task_description

# 4.
def get_long_task(list, time):
    long_tasks = []
    for task in list:
        if task["time_taken"] >= time:
            long_tasks.append(task)

    return long_tasks

# 5.
def get_specific_task(list, description):
    for task in list:
        if task["description"] == description:
            return task
            break

    return None

# 6.
def mark_complete_task(list, description):
    for task in list:
        if task["description"] == description:
            task["completed"] = True
            break

    #return None


'''
# 1. Print a list of uncompleted tasks
print("Question 1: ", get_uncompleted_tasks(tasks, False))

#P 2. rint a list of completed tasks
print("Question 2: ", get_uncompleted_tasks(tasks, True))

# 3. Print a list of all task descriptions
print("Question 3: ", get_descriptions(tasks))

# 4. Print a list of tasks where time_taken is at least a given time
print("Question 4: ", get_long_task(tasks, 15))

# 5. Print any task with a given description
print("Question 5: ", get_specific_task(tasks, "Feed Cat"))
print("Question 5: ", get_specific_task(tasks, "Feed Fish"))


#EXTENSION

# 6. Given a description update that task to mark it as complete.
mark_complete_task(tasks, "Feed Cat")
print("Question 6: ", tasks[3])

# 7. Add a task to the list

new_task = { "description": "Do Homework", "completed": False, "time_taken": 120 }
tasks.append(new_task)
print("Question 7: ", tasks)

'''

# 8. Use a while loop to display the following menu and allow the use to enter an option.
user_input = ""
while user_input != "Q" and user_input != "q":
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")

    user_input = input("Please select option: ")

    if user_input == "1":
        print(tasks)
    elif user_input == "2":
        print(get_uncompleted_tasks(tasks, False))
    elif user_input == "3":
        print(get_uncompleted_tasks(tasks, True))
    elif user_input == "4":
        print("Option 4 follows")
        complete_input = input("Please specify task: ")
        mark_complete_task(tasks, complete_input)
        for task in tasks:
            print(task["description"], task["completed"])
    elif user_input == "5":
        time = int(input("Please state length: "))
        get_long_task(tasks, time)
        print("Option 5 follows")
        for task in tasks:
            if task["time_taken"] >= time:
                print(task["description"], task["time_taken"])
    elif user_input == "6":
        complete_input = input("Please specify task: ")
        print(get_specific_task(tasks, complete_input))
    elif user_input == "7":
        user_description = input("Please enter task description: ")
        user_time_taken = int(input("Please enter length of task: "))
        new_task = { "description": user_description, "completed": False, "time_taken": user_time_taken }
        tasks.append(new_task)
        print(tasks)
    elif user_input == "M" or user_input == "m":
        continue
    else:
        continue






