# 113. Path Sum II
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22

# Ok this is similar to path Sum I, just that I need to append the values of the individual nodes into an array instead of just returning a boolean
# Expects an array as the output
# Needs a base case first
# Basically since the question mentioned from root all the way to leaf, my base case is these 2,
# 1. What to do when the root is None, I return an empty array?
# 2. What to do when a leaf node is reached, I return back the value of the node
# So I need to determine what I want the algo to do recursively
# Think in small tree
# Maybe not use the remainder?
# cos I need to calculate the sum of the calculated nodes and compare it

# Understanding after referring to GPT:
# So for this question I will need a helper function to store the path so far as well as to contain the recursive into one function
# so within the dfs helper function, I need to treat it like its a separate question, and this is where my dfs will happen
# so within the dfs function, I will need to pass in a node (Which is the node that it is currently on), the path so far, which is an array that contains all the node that we have added, and a current sum, as a variable to keep track of the current sum so far

# class Solution:
#     def hasPathSum(self, root, targetSum):
#         res = []  # an empty array to store all valid path

#         def dfs(node, path_so_far, current_sum):
#             if node is None:
#                 return
#             path_so_far = path_so_far + [node.val]
#             current_sum += node.val
#             if node.left is None and node.right is None:
#                 if current_sum == targetSum:
#                     res.append(path_so_far)

#             dfs(node.left, path_so_far, current_sum)
#             dfs(node.right, path_so_far, current_sum)

#         dfs(root, [], 0)


# a = Solution()
# a.hasPathSum(root, 3)
