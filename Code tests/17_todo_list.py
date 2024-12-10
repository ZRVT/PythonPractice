import csv
import json


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
    print('5. Export the todo list.')
    print('6. Exit the todo list application. \n')
    
    while True:
        try: 
            choice = int(input('Please make a choice from (1/6): '))
            if choice in [1,2,3,4,5,6]:
                return choice
                break
            else: 
                print('\nPlease provide a number from 1 to 6')
        except ValueError:
             print('\nPlease provide a number from 1 to 6')

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
        print(f'Task = {tasks["name"]} --- Completed = {tasks["completed"]}')

def task_completed() -> None:
    """This function marks a tasks as completed once it is done and over with. 
    """
    print('Please select the tasks you want to mark as completed\n')

    for tasks in todo_list:
        print(f'{tasks['name']}')
    while True: 
        completed_tasks = input('\n Please input the name of the task you want to complete: ').strip().lower()
        for tasks in todo_list:
            if tasks["name"] == completed_tasks:
                tasks["completed"] = True
                print(f'Task {tasks["name"]} is completed = {tasks["completed"]} ')
                return
        print('Please provide a valid input')

def task_deletion() -> None:
    """_summary_
    This function doesn't require an input and will delete the task the user chooses. 
    """
    print('Please choose the task you want to delete \n')

    for tasks in todo_list:
        print(f'{tasks["name"]}')
    
    while True:
        task_deleted = input('Please input the task name you want to delete.').strip().lower()
        for tasks in todo_list:
            if task_deleted == tasks['name']:
                print(f'\n____ You have removed task {tasks["name"]} ___')
                todo_list.remove(tasks)
                return

def export_todo_pogram() -> None:
    while True: 
        export_choice = input('Please choose between export options (csv,json,text): ')
        if export_choice in ("csv","json","text"):
            file_name = input("Enter the filename to export (e.g., todo_list.txt): ").strip()
            break
        else:
            print('Please provide a valid export choice. \n')
    
    #export to CSV section
    if export_choice == "csv":    
        try:
            with open(file_name, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["name", "completed"])
                writer.writeheader()
                writer.writerows(todo_list)
                print(f"\nTodo list successfully exported to {file_name}")
        except Exception as e:
            print(f"An error occurred while exporting: {e}")

    #export to JSON section.
    elif export_choice == "json":
        try:
            with open(file_name, 'w') as json_file:
                json.dump(todo_list, json_file, indent=4)
            print(f"\nTodo list successfully exported to {file_name}")
        except Exception as e:
            print(f"An error occurred while exporting to JSON: {e}")
            print("json")

    #export to TEXT file section. 
    elif export_choice == "text":    
        try:
            with open(file_name, 'w') as file:
                for task in todo_list:
                    file.write(f"Task: {task['name']}, Completed: {task['completed']}\n")
            print(f"\nTodo list successfully exported to {file_name}")
        except Exception as e:
            print(f"An error occurred while exporting: {e}")

todo_list = []

while True:
    choice = user_choice()
    if choice == 1:
        todo_list = add_task(input('Input your task here: ').strip().lower())
    elif choice == 2: 
        view_task()
    elif choice == 3:
        task_completed()
    elif choice == 4:
        task_deletion()
    elif choice == 5:
        export_todo_pogram()
    elif choice == 6:
        print('The todo list is now closing down.')
        break
