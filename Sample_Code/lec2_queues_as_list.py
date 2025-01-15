class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        else:
            return False
        
    def dequeue(self):
        if len(self.queue) <= 0:
            print("Queue is empty!!!")
        else:
            return self.queue.pop()
    
    def peek(self):
        return self.queue[-1]
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        if len(self.queue) <= 0:
            return True
        else:
            return False
        
    def show(self):
        return self.queue
        
my_q = Queue()
my_q.enqueue("Mon")
my_q.enqueue("Tue")
my_q.enqueue("Wed")
my_q.enqueue("Thu")
print("Queue size: {} contents: {} \n".format(my_q.size(), my_q.show()))


print("Peek: {} \n".format(my_q.peek()))

print("dequeue: {} Remaining: {}\n".format(my_q.dequeue(), my_q.show()))
print("dequeue: {} Remaining: {}\n".format(my_q.dequeue(), my_q.show()))
      