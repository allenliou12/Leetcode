# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]

# Example 3:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 4:
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


# So I can take intuition from the level order, meaning by each level I get the pair of val of the node at each level, and if there is one one number in that row, i take that number, if there is two then I take the second number
class Solution:
    def rightSideView(self, root):
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for i in range(level_size):  # For each level:
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)

            result.append(level_nodes[-1])

        return result


a = Solution()
print(a.rightSideView(p))
