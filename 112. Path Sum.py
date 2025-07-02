# # 112. Path Sum
# # Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# # A leaf is a node with no children.

# # Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# # Output: true

# # Ok so the intuition is that I need to iterate through each and every root to leave node, and compare if the sum is equals to target or not
# # So since I need to check every combination, from root to leaf, this will require me to use a dfs technique
# # So to start with the dfs technique, I need to set a base case first
# # The base case will be: If the root is None, return False, since the question is asking me to output boolean
# # I need a way to track the accumulated count
# # So maybe something like the fibonnacci number? like count = root.left + root.val
# # So if the val is = target, return True


# class Solution:
#     def hasPathSum(self, root, targetSum):
#         if root is None:
#             return False
#         if root.left is None and root.right is None:
#             return root.val == targetSum
#         remaining = targetSum - root.val
#         left = self.hasPathSum(root.left, remaining)
#         right = self.hasPathSum(root.right, remaining)

#         return left or right


# a = Solution()
# a.hasPathSum(root, 3)

# 112.Path Sum (Reattempt using a helper function)
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.
# Since we need to go through from root to leaf node, we need to use the dfs technique
# So that means we need a base case and recursive case
# So what is the base case
# Simple term, if the root is none, then we return False,
# So we need to keep track of the current sum all the way until we reach the leaf node
# and how we know its a leaf node?
# If there are no left and right then its a leaf node
# So if its at the leaf node already, we need to check if the current sum is equals to target or not, if yes we return True


class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        def dfs(node, current_sum):
            if node is None:
                return False
            current_sum += node.val
            if node.left is None and node.right is None:
                if current_sum == targetSum:
                    return True
            return dfs(node.left, current_sum) or dfs(node.right, current_sum)

        return dfs(root, 0)


a = Solution()
print(a.hasPathSum(p, 4))
