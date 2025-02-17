import networkx as nx
import  matplotlib.pyplot as plt



class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def insert(self, key):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
            else:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insert(key)
        else:
            self.key = key

    def search(self, root, key):
        if root is None:
            return root
        else:
            if root.key == key:
                return root
            elif root.key < key:
                return self.search(root.right, key)
            else:
                return self.search(root.left, key)

    def findMin(self, root):
        if root is None:
            return None
        while root.left is not None:
            root = root.left

        return root

    def findMax(self, root):
        if root is None:
            return None
        while root.right is not None:
            root = root.right

        return root

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is not None and root.right is not None:
                temp = self.findMin(root.right)
                root.key = temp.key
                del temp
                return root

            elif root.left is None:
                temp = root.right
                del root
                return temp
            else:
                temp = root.left
                del root
                return temp
        return root
    def printTree(root):
        if root.left:
            root.left.printTree(root.left)
        print(root.key)
        if root.right:
            root.right.printTree(root.right)

    def PreorderTraversal(self, root):
        result = []
        def dfs(root):
            if root is None:
                return
            result.append(root.key)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return result

    def visualize_binary_tree(self):
        G = nx.Graph()
        G.add_node(str(self.key))
        def add_Node_Edge(root):
            if root.left:
                G.add_node(str(root.left.key))
                G.add_edge(str(root.key), str(root.left.key))
                add_Node_Edge(root.left)
            if root.right:
                G.add_node(str(root.right.key))
                G.add_edge(str(root.key), str(root.right.key))
                add_Node_Edge(root.right)

        add_Node_Edge(self)
        nx.draw_networkx(G, with_labels=True)
        plt.show()



tree = Node(27)
tree.insert(14)
tree.insert(35)
tree.insert(10)
tree.insert(19)
tree.insert(31)
tree.insert(42)
#visualize_binary_tree(tree)

#print(tree.PreorderTraversal(tree))

#print(tree.inorderTraversal(tree))

#print(tree.PostorderTraversal(tree))

tree.visualize_binary_tree()
tree.delete(tree, 27)
#print(tree.PreorderTraversal(tree))
tree.visualize_binary_tree()
a = tree.search(tree, 3)
print(a.key if a else None)



