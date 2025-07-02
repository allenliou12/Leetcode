# # 101. Symmetric Tree
# # Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# # Ok so this is similar to a question I attempted earlier, of comparing trees
# # I need to compare a tree, check if the left and right is the same or not
# # Recursively check it for the whole tree
# # I will need a base case:
# # If root is None return False (Return False since the question is asking an output of boolean)
# # I need to match the mirror
# # Mirror is when the left node is at the right node
# # I would need to go down all the way from root to leaf node. Do I need to store the values?


# class Solution:
#     def isSymmetric(self, root):
#         if root is None:
#             return True

#         def isMirror(left, right):
#             if left is None and right is None:
#                 return True
#             if left is None or right is None:
#                 return False
#             if left.val != right.val:
#                 return False
#             return isMirror(left.left, right.right) and isMirror(left.right, right.left)

#         return isMirror(root.left, root.right)
