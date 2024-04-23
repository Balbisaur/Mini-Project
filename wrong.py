
while True:
    print('''
        Welcome to the To-Do-List App!
        ******************************
        Choose an Action
        ----------------
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete task
        5. Quit
        ''')
    try:
        action = input('Action: ')
        if not action in ['1', '2', '3', '4', '5']:
            raise ValueError
    except ValueError:
        print('Selection not available, please choose 1, 2, 3, 4, or 5')
    except:
        print('Invalid Input')
    else:
        if action == '1':
            print('Adding new tasks')
            tasks = input('Names of tasks: ')
            print(action)
        elif action == '2':
            print('Viewing all current tasks')
            print('List of tasks: ')
            action = len(input(tasks))
            
            break
        elif action == '3':
            print('which task would you like to mark as complete? ')
        
        elif action == '4':
            print('Which task would you like to delete? ')
        
        elif action == '5':
            print('Exitting App, Come Back Soon!')
            break

#This is how I was first doing the project.
#I thought I was doing it right. I was able to add a task and view the task
#but was never able to find out how to mark the task as complete or delete a certain task.
#Then during pre-class, I saw the similar example we were doing and noticed I wasn't using *def* functions.
#So I decided to scrap this one and start over.
# I dont know if I was still doing it right but a different version
#im going to keep my first attempt here so you can possibly give me feedback on what I was doing wrong.