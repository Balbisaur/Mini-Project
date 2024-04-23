
def add_to_task(tasks, task):
    tasks.append({"Title": task, "Status": 'incomplete'})

def viewing_tasks(tasks):
    if not tasks:
        print("No tasks currently.")
        return
    print("Tasks:")
    for idx, task in enumerate(tasks, start=1):
         print(idx, {task["Title"]})
         

def mark_as_complete(tasks):
    pass
    


def delete_task(to_do_list, task_index):
    try:
        idx = int(task_index)
        if 1 <= idx <= len(to_do_list):
            to_do_list[task_index - 1]
            print('Task has been removed')
        else:
            print('Invalid Index')
    except ValueError:
        print('Invalid Input. enter a valid input.')


def to_do_list():
    tasks = []
    
    while True:
        print("""
    ################################
    |Welcome to the To-Do List App!|
    |-----                         |
    |Menu:                         |
    |1. Add a task                 |
    |2. View tasks                 |
    |3. Mark a task as complete    |
    |4. Delete a task              |
    |5. Quit                       |
    ################################
    """)
        action = input("Enter your action: ")
        try:
            action = int(action)
            if action == 1:
                task = input("Enter new task: ")
                add_to_task(tasks, task)
            elif action == 2:
                viewing_tasks(tasks)
            elif action == 3:
                pass
            elif action == 4:
                print(input('which {idx} would you like to remove? '))
            elif action == 5:
                print("Exitting Application. Come Back Soon!")
                break
            else:
                print("Invalid Selection. Choose a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")


to_do_list()


#This is my second attempt with using the *def functions.
#I was able to add a task,
#when I view task with just *for i, task in enumerate(tasks). The list of tasks starts at 0
#so I added *for i, task in enumerate(tasks, start=1). So whenever I view my tasks, it starts with *1.
#Now I am still lost on how to mark each task as complete and delete a certain task
#I also incorporated *enumerate() into my program, that we learned from yestersays class, so I can have my tasks listed starting from *idx 1.
#also having trouble giving the task the incomplete status.