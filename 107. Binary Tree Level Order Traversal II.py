# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

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
q.left.left = TreeNode(3)
q.right.right.left = TreeNode(5)

# Same as the level order, I just need to reverse the final result


class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        res = []
        queue = deque([root])
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

            res += [level_node]

        return res[::-1]


a = Solution()
print(a.levelOrderBottom(p))
