# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Ok so this is a BFS question. A BFS qustion always have a queue and a visited
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p = TreeNode(3)
p.left = TreeNode(1)
p.right = TreeNode(5)


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for i in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)

            result += [level_nodes]

        return result


a = Solution()
print(a.levelOrder(p))
