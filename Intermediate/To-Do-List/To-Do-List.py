# create to do list
inputting = True
tdl = {} # start with an empty dictionary to hold the tasks.
while inputting == True: # while loop to add tasks, and check if user wants to add more
    inputting = input("Would you like to add another item? (yes/no): ")
    if inputting == "yes":
        inputting = True
        task = input("Enter a task to add to your to-do list: ")
        tdl[task] = False # Initially set task as False as it indicates task is incomplete
    elif inputting == "no":
        inputting = False
    else : 
        print("Invalid input. Please enter 'yes' or 'no'.")
        inputting = False
print(tdl)
# mark tasks as complete
for task in tdl: # for loop to iterate through tasks and mark them as complete or imcomplete
    complete = input("Have you completed the task '" + task + "'? (yes/no): ")
    if complete == "yes":
        tdl[task] = complete = True
    elif complete == "no":
        tdl[task] = complete =False
    else: 
        print("Invalid input. Please enter 'yes' or 'no'.")
print(tdl)

# display completed tasks
print("Completed tasks:")
for task, status in tdl.items():
    if status == True:
        print("- " + task)
# display incomplete tasks
print("Incomplete tasks:")
for task, status in tdl.items():
    if status == False:
        print("- " + task)

    