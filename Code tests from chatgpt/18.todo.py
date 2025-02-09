def userChoice ()-> int:
    
    print('\n Please fill in a choice below')
    print('1. Add a task')
    print('2. Views tasks')
    print('3. Complete tasks')
    
    while True:
        try: 
            choice = int(input('\nChoose a number from 1 to 6: '))
            if choice in [1,2,3,4,5,6]:
                return choice
                break
            else:
                print('Please fill in a choice from 1 to 6 only!')
        except ValueError:
            print('Please fill in a choice from 1 to 6 only!')

def addTask (task: str) -> list[dict[str,bool]] :
    """
    This will add the task into the task list.

    Args:
        task (str): _description_

    Returns:
        list[dict[str,bool]]: _description_
    """
    taskList.append({"TaskName": task, "Completed": False})
    print(f'\n You have added task: {task}')
    return taskList

def viewTasks() -> str:
    print('\nYou have the following tasks in your todo list \n')
    for tasks in taskList:
        print(f'The task: {tasks["TaskName"]} with status completed: {tasks["Completed"]}.')

def completeTask ():
    print('\n___ What task would you like to complete? ___ \n')
    viewTasks()
    while True:
        completeTask = input('\nWhat tasks to complete? : ').upper().strip()
        for tasks in taskList:
            if tasks["TaskName"] == completeTask:
                tasks["Completed"] = True
                print(f'The task {tasks["TaskName"]} is now completed')

                return taskList
        else:
            print('Please provide a valid input from the below tasks')
            viewTasks()

taskList = []

while True:
    choice = userChoice()
    if choice == 1:
        taskList = addTask(input('\n What task do you want to add? ').strip().upper())
    elif choice == 2:
        viewTasks()
    elif choice == 3:
        completeTask() 
    else:
        pass

    
