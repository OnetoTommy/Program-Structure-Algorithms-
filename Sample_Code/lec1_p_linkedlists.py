class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list.")
            return
        node = Node(data)
        node.next = prev_node.next
        prev_node.next = node

    def delete_node(self,key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

#Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print("Original linked list:")
linked_list.display()

linked_list.insert_at_beginning(0)
print("\nLinked list after inserting at the beginning:")
linked_list.display()

linked_list.insert_after_node(linked_list.head.next, 10)
print("\nLinked list after inserting after a specific node:")
linked_list.display()

linked_list.delete_node(2)
print("\nLinked list after deleting a node:")
linked_list.display()

