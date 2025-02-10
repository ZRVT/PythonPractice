import uuid

class Tasks:
    def __init__(self, name:str,completed,listId:int):
        self.id = str(uuid.uuid4())
        self.name = name
        self.completed = completed
        self.listId = listId

    def completeTasks(self):
        if self.completed == True:
            print("The task is already completed")
        else: 
            self.completed = True
            print(f'The tasks {self.name} is completed.')

    def deleteTask():
        pass

    