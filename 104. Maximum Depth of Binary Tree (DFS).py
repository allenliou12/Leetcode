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
q.left.left = TreeNode(7)
q.right.right.left = TreeNode(5)


# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2


# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

def maxDepth(self, root):
    if not root:
        return 0

    if root.left is None and root.right is None:  # Meaning only 1 node in tree
        return 1

    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return 1 + max(left, right)
