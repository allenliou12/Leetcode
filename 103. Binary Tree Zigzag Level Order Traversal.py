# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

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
q.left.left = TreeNode(7)
q.right.right.left = TreeNode(5)

# This is almost the same as other BFS question, just that I need a count for the levels, if its odd level, i take the 1st one in the pair of nodes


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        res = []
        level_count = 0
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

            level_count += 1

            if level_count % 2 == 0:
                res += [level_node[::-1]]
            else:
                res += [level_node]

        return res


a = Solution()
print(a.zigzagLevelOrder(q))
