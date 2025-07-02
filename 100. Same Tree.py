# # 100. Same Tree
# # First intuition, to use a dfs technique to go through each and every node in the tree
# # How to answer the question if the tree is same?
# # Condition 1: They have same structure, they have the same number of child nodes
# # Condition 2: The values of the child nodes needs to be same
# # Condition 3: The position of the child nodes needs to be the same
# # So condition 2 & 3 can be answered by this? p.left == q.left, p.right == q.right

# # So for dfs I need to set a base case first, what is the base case?
# # To keep going until there is no child left, return NONE?


# class Solution:
#     def isSameTree(self, p, q) -> bool:
#         # First we list out the conditions to be met to determine if the trees are same or not
#         # If there is nothing on p and q then they are the same
#         # This is the base case, !! REMEMBER THE BASE CASE DOESNT HAVE TO ALWAYS RETURN NONE, IT DEPENDS ON THE QUESTION
#         if q is None and p is None:
#             return True
#         # But if only either one is None but the other is populated then they are not the same
#         if p is None or q is None:
#             return False

#         # If both p and q are the same structure, check if the values are the same or not
#         if p.val != q.val:
#             return False

#         # Recursively do that for the child nodes
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# # 100. Same Tree (Reattempt)
# # Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# # Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# # Ok so for this I need to go through each and every node, so a dfs technique is required
# # So for a dfs algo I need 2 things:
# # 1.Base case
# # 2.Recursive case
# # Base case:
# # Since we are comparing p and q, what happens when both of them are None
# # If both of them are None, this means that they are the same
# # so we return True like the question asked
# # If either one is None, then we return False since they are not the same anymore
# # If they are not None and if they have the same value and their children is the same, ONLY THEN they are considered the same
# #


# class Solution:
#     def isSameTree(self, p, q):
#         if p is None and q is None:
#             return True
#         if p is None or q is None:
#             return False
#         if p.val == q.val:
#             return self.isSameTree(p.left, q.left) is True and self.isSameTree(p.right, q.right) is True
#         else:
#             return False
