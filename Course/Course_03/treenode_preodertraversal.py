class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution():

    def preorder(self, root: TreeNode):
        def traversal(root, res):
            if root == None:
                return

            res.append(root.val)
            traversal(root.left, res)
            traversal(root.right, res)

        res = list()
        traversal(root, res)
        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()
result = solution.preorder(root)
print("Preorder Traversal:", result)