class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueLL:
    def __init__(self):
        self.size = 0
        self.front = self.rear = None
        
    def isEmpty(self):
        return self.front == None
    
    def peek(self):
        return self.front.value
    
    def sizeOf(self):
        return self.size
    
    # Enqueue an item to the queue
    def enqueue(self, item):
        new_node = Node(item)
        self.size = self.size + 1

        if self.rear == None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    # Dequeue an item from the queue
    def dequeue(self):
        if self.isEmpty():
            return None
        self.size = self.size - 1
        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None
        return temp.value
        
    def show(self):
        out = list()
        if self.isEmpty():
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            out.append(temp.value)
            #print(temp.value, end=" ")
            temp = temp.next
        #print()
        return out


# Example usage
q = QueueLL()
q.enqueue("Mon")
q.enqueue("Tue")
q.enqueue("Wed")
q.enqueue("Thu")

print("Queue size: {} Contents: {}".format(q.sizeOf(), q.show()))

print("Peek: {} \n".format(q.peek()))

print("dequeue: {} Remaining: {}\n".format(q.dequeue(), q.show()))
print("dequeue: {} Remaining: {}\n".format(q.dequeue(), q.show()))

