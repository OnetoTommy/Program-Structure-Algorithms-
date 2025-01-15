class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def is_empty(self):
        return self.first == None

    def sizeof(self):
        return self.size

    def peek(self):
        if self.is_empty():
            return None
        return self.first.value

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.first = self.last = node
        self.size +=1
        self.last.next = node
        self.last = node

    def dequeue(self):
        if self.is_empty():
            return None
        self.size -=1
        temp = self.first
        self.first = temp.next

        if self.first == None:
            self.last = None
        return temp.value

    def show(self):
        showlist = list()
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.first
        while temp != None:
            showlist.append(temp.value)
            temp = temp.next
            self.size -=1

        return showlist




# Example usage
q = Queue()
q.enqueue("Mon")
q.enqueue("Tue")
q.enqueue("Wed")
q.enqueue("Thu")

print("Queue size: {} Contents: {}".format(q.sizeof(), q.show()))

print("Peek: {} \n".format(q.peek()))

print("dequeue: {} Remaining: {}\n".format(q.dequeue(), q.show()))
print("dequeue: {} Remaining: {}\n".format(q.dequeue(), q.show()))
