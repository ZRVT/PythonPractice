def user_choice() -> int:
    """ Function that allow the user to input their choice and returns a integer value. 

    Returns:
        int: Return the choice of the user in a integer from 1 to 5 \n
        \n 1 = Add tasks
        \n 2 = View all tasks
        \n 3 = Mark task completed
        \n 4 = Delete a tasks
        \n 5 = Exit todo list
    """
    print('\n1. Add a task')
    print('2. View all tasks')
    print('3. Mark task completed.')
    print('4. Delete a tasks.')
    print('5. Exit todo list.\n')
    choice = int(input('Please make a choice from (1/5): '))
    while True:
        try: 
            if choice in [1,2,3,4,5]:
                return choice
                break
            else: 
                print('Please provide a number from 1 to 5')
        except ValueError:
             print('Please provide a number from 1 to 5')

def add_task(task: str) -> list[dict[str,bool]]:
    """Simple function to add a task to the todo list application. 

    Args:
        task (str): Input the task name as the argument. 

    Returns:
        list[dict[str,bool]]: It will generate an a new item in the todo list and mark it as completed = false
    """
    todo_list.append({"name":task, "completed":False })
    print(f'\n You have add the task: {task} to your list.\n')
    return todo_list

def view_task() -> None:
    """ Returns all the tasks with a for loop

    Returns:
        str: prints our the task and the status of the tasks. 
    """
    for tasks in todo_list:
        print(f'Task = {tasks['name']} --- Completed = {tasks['completed']}')

def task_completed() -> None:
    """This function marks a tasks as completed once it is done and over with. 
    """
    print('Please select the tasks you want to mark as completed\n')

    for tasks in todo_list:
        print(f'{tasks['name']}')
    while True: 
        completed_tasks = input('\n Please input the name of the task you want to complete: ').strip().upper()
        for tasks in todo_list:
            if tasks["name"] == completed_tasks:
                tasks["completed"] = True
                print(f'Task {tasks['name']} is completed = {tasks['completed']} ')
                return
        print('Please provide a valid input')

def task_deletion() -> None:
    """_summary_
    This function doesn't require an input and will delete the task the user chooses. 
    """
    print('Please choose the task you want to delete \n')

    for tasks in todo_list:
        print(f'{tasks['name']}')
    
    while True:
        task_deleted = input('Please input the task name you want to delete.').strip().upper()
        for tasks in todo_list:
            if task_deleted == tasks['name']:
                print(f'\n____ You have removed task {tasks['name']} ___')
                todo_list.remove
                return

def exit_todo_pogram():
    pass

todo_list = []

while True:
    choice = user_choice()
    if choice == 1:
        todo_list = add_task(input('Input your task here: ').strip().upper())
    elif choice == 2: 
        view_task()
    elif choice == 3:
        task_completed()
    elif choice == 4:
        task_deletion()
    elif choice == 5:
        print('The todo list is now closing down.')
        break
