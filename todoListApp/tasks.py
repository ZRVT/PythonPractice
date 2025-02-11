import uuid

class Tasks:
    def __init__(self, name:str,listId:int =  0):
        """This class makes a tasks.

        Args:
            name (str): Mandatory field and required
            listId (int): Not mandatory field and not required.
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.completed = False
        self.listId = listId
    
    def __post_init__(self):
        # This function gives error if task name not added
        if not self.name or self.name.strip() == "":
            raise ValueError("Task name is required")

    def completeTasks(self):
        if self.completed == True:
            print("The task is already completed")
        else: 
            self.completed = True
            print(f'The tasks {self.name} is completed.')

    def deleteTask(self):
        pass

task_list = []


task_list.append(Tasks())

print(task_list)