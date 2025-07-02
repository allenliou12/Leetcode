class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(1)


q = TreeNode(1)
q.left = TreeNode(1)
q.right = TreeNode(2)
