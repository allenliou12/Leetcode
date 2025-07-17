# Not understood, Dont copy GPT answer, leave for future comeback


# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

# I have to go through from each root to leaf node. Then return the minimum for left tree and right tree
# Since I have to go through every node, this calls for the DFS approach
# Base Case:
# if root is None then return 0 becos None means there is no Node
# If there is a node, and its the only node, then the depth is 1
# Recursive Case:
#

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


class Solution:
    def minDepth(self, root) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        if root.left is None and root.right is not None:
            return 1 + self.minDepth(root.right)

        if root.right is None and root.left is not None:
            return 1 + self.minDepth(root.left)

        if root.right is not None and root.left is not None:
            return 1+min(self.minDepth(root.right), self.minDepth(root.left))


a = Solution()
print(a.minDepth(q))
