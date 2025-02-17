import networkx as nx
import matplotlib.pyplot as plt
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def visualize_binary_tree(root):
    dot = nx.DiGraph()
    dot.add_node(str(root.data))

    def add_nodes_edges(node):
        if node.left:
            dot.add_node(str(node.left.data))
            dot.add_edge(str(node.data), str(node.left.data))
            add_nodes_edges(node.left)
        if node.right:
            dot.add_node(str(node.right.data))
            dot.add_edge(str(node.data), str(node.right.data))
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    nx.draw_networkx(dot)
    plt.show()

def show_tree(root, type):
    if root is None:
        return
    else:
        print("%d:%s"%(root.data, type))
    
    #print left subtree
    if root.left is not None:
        show_tree(root.left, type+"L")

    if root.right is not None:
        show_tree(root.right, type+"R")

class BinaryHeap:
    def __init__(self):
        self.root = None

    def build_heap(self, array):
        root = Node(array[0])
        for i in range(1, len(array)):
            self.insert(root, array[i])

        return root

    def insert(self, root, data):
        if root is None:
            return Node(data)
    
        if root.left is not None:
            if root.right is None:
                root.right = Node(data)
            else:
                self.insert(root.left, data)
        else:
            root.left = Node(data)

        self.heapify(root)

    def heapify(self, root):
        if root is None:
            return
    
        left = root.left
        right = root.right

        if left is not None and left.data > root.data:
            root.data, left.data = left.data, root.data
            self.heapify(left)

        if right is not None and right.data > root.data:
            root.data, right.data = right.data, root.data
            self.heapify(right)


    def findLast(self, root):
        if root is None:
            return None
    
        if root.left is None and root.right is None:
            return root
        else:
            if root.right is not None:
                return self.findLast(root.right)
            elif root.left is not None:
                return self.findLast(root.left)

    def deleteLast(self, root, last):
        if root is last:
            root = None
            return
    
        if root.left is not None:
            if root.left is last:
                root.left = None
            else:
                self.deleteLast(root.left, last)

        if root.right is not None:
            if root.right is last:
                root.right = None
            else:
                self.deleteLast(root.right, last)


    def deleteNode(self, root):
        if root is None:
            return
        last = self.findLast(root)
        root.data = last.data
        self.deleteLast(root, last)
    

    def heap_sort(self, array):
        root = self.build_heap(array)
        visualize_binary_tree(root)
        
        for i in range(len(array) - 1, -1, -1):
            array[i] = root.data
            #print("Value at index %d is %d"%(i, array[i]))
            self.deleteNode(root)
            self.heapify(root)
            #visualize_binary_tree(root)
    

        return array

# Example usage:

t = BinaryHeap()
array1 = [5, 3, 2, 1, 4]
sorted_array = t.heap_sort(array1)

array2 = []
for _ in range(20):
    val = random.randint(1, 100)
    array2.append(val)
print(array2)
sorted_array = t.heap_sort(array2)
print(sorted_array)