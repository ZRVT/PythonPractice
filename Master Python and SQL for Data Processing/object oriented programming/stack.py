class Stack:
    def __init__(self):
        # Initialize an empty stack
        self.stack = []

    def push(self, item):
        # Push the item onto the stack
        self.stack.append(item)

    def pop(self):
        # Remove and return the item at the top of the stack
        if self.is_empty():
            raise IndexError("can't pop from empty stack")
        self.stack.pop()
        #pop already removes from the last item from the list. No need to use an index here. 
    def peek(self):
        # Return the item at the top of the stack without removing it
        if self.is_empty():
            return None 
        return self.stack[-1]
    
    def is_empty(self):
        # Return True if the stack is empty, False otherwise
        if self.is_empty():
            return True
        else:
            False

    def size(self):
        # Return the number of items in the stack
        return len(self.stack)