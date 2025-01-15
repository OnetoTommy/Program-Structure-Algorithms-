from glob import escape
from operator import truediv


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        if value not in self.queue:
            self.queue.insert(0, value)
            return True
        else:
            return False

    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        else:
            return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        else:
            return self.queue[0]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

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
