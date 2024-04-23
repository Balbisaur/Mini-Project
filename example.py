today = 'woke up', 'ate breakfast', 'walked my dog', 'prepped lecture', 'ate lunch', 'graded', 'meetings', 'in class'

for task in enumerate(today): #task is a tuple of the index and item
    print(task[1])

print('--------------------')

for idx, task in enumerate(today):
    print(idx)
    print(task)