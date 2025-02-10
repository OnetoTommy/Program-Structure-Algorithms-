class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution():
    def isSymmetric(self, root:TreeNode) :
        if not root:
            return True

        def symmetry(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 and not t2:
                return False
            return (t1.val == t2.val and symmetry(t1.left, t2.right) and symmetry(t1.right, t2.left))

        return symmetry(root.left, root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()
result = solution.isSymmetric(root)
print("Preorder Traversal:", result)