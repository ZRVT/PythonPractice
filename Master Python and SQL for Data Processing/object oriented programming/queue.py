class Queue:
    def __init__(self):
        # Initialize an empty queue
        self.queue = []

    def enqueue(self, item):
        # Add the item to the back of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        if self.is_empty():
            raise IndexError("can't dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self):
        # Return the item at the front of the queue without removing it
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        # Return True if the queue is empty, False otherwise
        return len(self.queue) == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.queue)