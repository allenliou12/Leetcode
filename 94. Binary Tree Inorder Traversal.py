# # 94. Binary Tree Inorder Traversal
# # Given the root of a binary tree, return the inorder traversal of its nodes' values.
# # Input: root = [1,null,2,3]
# # Output: [1,3,2]

# # So for this question I need to print out the node when it travels there
# # I still need to implement DFS, just that in this question I need to append the value of the root onto an array and return that array
# # Think in the smallest tree first
# # So the base case is if the node has NONE, do something, what is this something? if there is nothing else left, just return the arr
# # Because the question is asking Inorder Traversal, that means the algo will need to visit the left node first, then move back to root then the right node
# class Solution:
#     def __init__(self) -> None:
#         self.arr = []

#     def inorderTraversal(self, root):
#         if root is None:
#             return self.arr

#         # If there are child node

#         # Recursively do that for left and right node
#         self.inorderTraversal(root.left)
#         self.arr.append(root.val)
#         self.inorderTraversal(root.right)

#         return self.arr
