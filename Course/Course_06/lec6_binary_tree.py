import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.key = data

    # Insert Node
    def insert(self, data):
        if self.key:
            if data < self.key:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.key:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.key = data

    def search(root, key):
        # Base Cases: root is null or key is present at root
        if root is None or root.key == key:
            return root
 
        # Key is greater than root's key
        if root.key < key:
            return search(root.right, key)
 
        # Key is smaller than root's key
        return search(root.left, key)

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
        if root == None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
            return root
        elif key > root.key:
            root.right = self.delete(root.right, key)
            return root
        
        ## One child case
        if root.left is None:
            temp = root.right
            del root
            return temp
        elif root.right is None:
            temp = root.left
            del root
            return temp
        else: 
            ## two children case
            succParent = root
            ## find successor
            succ = self.findMin(root.right)
            #succ = self.findMax(root.left)
            
            #while succ.left is not None:
            #    succParent = succ
            #    succ = succ.left
            #if succParent != root:
            #    succParent.left = succ.right
            #else:
            #    succParent.right = succ.right
            root.key = succ.key
            del succ
            return root

    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.key)
        if self.right:
            self.right.PrintTree()

    # Preorder traversal
    # Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.key)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.key)
            res = res + self.inorderTraversal(root.right)
        return res
    
    # Postorder traversal
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.key)
        return res
    
def visualize_binary_tree(root):
    dot = nx.Graph()
    dot.add_node(str(root.key))

    def add_nodes_edges(node):
        if node.left:
            dot.add_node(str(node.left.key))
            dot.add_edge(str(node.key), str(node.left.key))
            add_nodes_edges(node.left)
        if node.right:
            dot.add_node(str(node.right.key))
            dot.add_edge(str(node.key), str(node.right.key))
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    nx.draw_networkx(dot)
    plt.show()
    
tree = Node(27)
tree.insert(14)
tree.insert(35)
tree.insert(10)
tree.insert(19)
tree.insert(31)
tree.insert(42)
#visualize_binary_tree(tree)

print(tree.PreorderTraversal(tree))  

print(tree.inorderTraversal(tree))  

print(tree.PostorderTraversal(tree))  

visualize_binary_tree(tree)
#tree.delete(tree, 27)
#print(tree.PreorderTraversal(tree))  
#visualize_binary_tree(tree)