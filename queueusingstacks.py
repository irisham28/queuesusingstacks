class Queueusingstacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        # Push the new item onto stack1
        self.stack1.append(item)

    def dequeue(self):
        # If stack2 is empty, transfer all elements from stack1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, the queue is empty
        if not self.stack2:
            return "Queue is empty"
        
        # Pop from stack2
        return self.stack2.pop()

# Example usage:
queue = Queueusingstacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  
print(queue.dequeue())  
queue.enqueue(4)
print(queue.dequeue())  
print(queue.dequeue()) 