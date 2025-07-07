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
# Recursive Case:
# else I have to
# I have to return the min(recurse(left),recurse(right))


class Solution:
    def minDepth(self, root) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1


a = Solution()
print(a.minDepth(q))
