class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        if item not in self.stack:
            self.stack.append(item)
            return True
        else:
            return False

    def pop(self):
        if len(self.stack) <= 0:
            return
        return self.stack.pop()

    def peek(self):
        if len(self.stack) <= 0:
            return
        else:
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def show(self):
        print(self.stack)

my_stack = Stack()
my_stack.push("Mon")
my_stack.push("Tue")
print("Peek: {} \n".format(my_stack.peek()))
my_stack.push("Wed")
my_stack.push("Thu")
print("Stack contents: {} \n".format(my_stack.show()))

print("Peek: {} \n".format(my_stack.peek()))

print("Pop: {} Remaining: {}\n".format(my_stack.pop(), my_stack.show()))
print("Pop: {} Remaining: {}\n".format(my_stack.pop(), my_stack.show()))