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
