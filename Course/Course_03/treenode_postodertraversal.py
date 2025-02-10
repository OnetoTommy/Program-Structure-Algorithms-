class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class solution():
    def postorderTraversal(self, root:TreeNode):
        def postorder(root, res):
            if root == None:
                return
            postorder(root.left, res)
            postorder(root.right, res)
            res.append(root.val)

        res = list()
        postorder(root, res)
        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = solution()
result = solution.postorderTraversal(root)
print("Preorder Traversal:", result)