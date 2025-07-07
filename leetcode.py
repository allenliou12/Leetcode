class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p = TreeNode(3)
p.left = TreeNode(1)
p.right = TreeNode(5)


q = TreeNode(1)
q.left = TreeNode(1)
q.right = TreeNode(2)
q.right.right = TreeNode(3)
q.left.left = TreeNode(3)
q.right.right.left = TreeNode(5)

