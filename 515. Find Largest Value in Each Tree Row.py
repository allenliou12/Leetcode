# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]

# Example 2:
# Input: root = [1,2,3]
# Output: [1,3]


# Constraints:
# The number of nodes in the tree will be in the range [0, 104].
# -231 <= Node.val <= 231 - 1

from collections import deque


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

# Ok so for each level of nodes, I need to compare their values, so I need to return maybe something like the max(level_nodes)?


class Solution:
    def largestValues(self, root):
        if not root:
            return []
        queue = deque([root])
        res = []

        while queue:
            level_size = len(queue)
            level_node = []

            for i in range(level_size):
                node = queue.popleft()
                level_node.append(node.val)

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)

            res.append(max(level_node))

        return res


a = Solution()
print(a.largestValues(p))
