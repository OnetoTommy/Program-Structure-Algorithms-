class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front == None

    def sizeof(self):
        return self.size

    def peek(self):
        return self.front.value

    def enqueue(self, value):
        node = Node(value)
        self.size += 1
        if self.is_empty():
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node


    def dequeue(self):
        if self.is_empty():
            return None
        self.size -= 1
        temp = self.front
        self.front = temp.next

        if self.front == None:
            self.rear = None
        return temp.value


    def show(self):
        showlist = list()
        if self.is_empty():
            print('Queue is empty')
            return
        temp = self.front
        while temp != None:
            showlist.append(temp.value)
            temp = temp.next

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
