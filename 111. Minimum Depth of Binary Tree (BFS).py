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

# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5


# Constraints:
# The number of nodes in the tree is in the range [0, 105].
# -1000 <= Node.val <= 1000

# So what im thinking is that we know the answer that the min depth of a tree ends either where the part where that level has no child anymore, or specifically, one of the node in that level has no more child nodes.

# So we just need to count the levels until either we reached a level where one of the nodes has no more child, or when we reach the end of a tree

# Thinking, since we are using bfs, we need to keep a queue. so if there is no root, then the min depth is 0, but if there is only 1 node, then the min depth is one.

# SO In other words depending the level, level 1 it only has 1 node, level 2 = 2 node, level 3 =4, level 4 will have 8. Meaning starting from level 1, all following level must have that level x 2?, a level doesn meet this criteria already, meaning its at the min depth

# Well Im dum, I dont need to check everything. I just need to stop the moment when I hit a leaf node

class Solution:
    def minDepth(self, root) -> int:
        level = 0
        if not root:
            return level
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                if node.left == None and node.right == None:
                    return level + 1
            level += 1
        return level


a = Solution()
print(a.minDepth(q))
