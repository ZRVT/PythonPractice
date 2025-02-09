# The below is a class and it has attributes 
class car:
    """This is to test out how this looks
        Basically this is a car that drives on 4 wheels
    """
    def __init__(self,make:str,model:str,year:int,color:str):
        self.make = make
        self.model = model
        self.year = year
        self.color = color


# The below are methods of the class 
    def drive(self):
        """This function will share if the car is driving
        """
        print(f"This {self.model} is driving")
    
    def stop(self):
        """This function will share if the car is stopping
        """
        print(f"This {self.model} is stopping")