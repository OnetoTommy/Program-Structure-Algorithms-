#from graphviz import Digraph

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            return
        prev.next = current.next
        current = None

    def visualize(self, filepath='./'):
         dot = Digraph(comment='The Linked List')

         current = self.head
         i = 0
         while current:
             dot.node(str(i), str(current.data))
             if i > 0:
                  # Add an edge from the previous node to this one
                 dot.edge(str(i - 1), str(i))
             current = current.next
             i += 1

         # Render the graph to a file
         filename = filepath +'linked_list'
         dot.render(filename, format='png', view=True)
         print(f"Linked list visualization rendered as '{filename}.png'")

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

#linked_list.visualize()