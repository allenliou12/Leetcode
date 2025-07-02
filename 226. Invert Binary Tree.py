# # 226. Invert Binary Tree
# root = [2, 1, 3]
# # Output: [2,3,1]


#  Ok breakdown of the function step by step

# The root is 2, we first check invertTree(2)
# Since 2 has 2.left and 2.right, so the return None condition is not met
# we get the left child first, which is invertTree(1), but since it has no left and right child, we swap nothing, and then we returned the root (1) back as left
# Then we deal with the right tree (the 3), which is invertTree(3), but since it has no child, we swapped nothing and then we returned the root 3 back as right
# We then continue to swap left and right and then return the root (THIS SWAP ALMOST HAPPENS LAST, MEANING IF THERE ARE CHILD NODES IN THE LEFT AND RIGHT, IT WILL KEEP GOING UNTIL THERE ARE NONE LEFT, AND THEN SWAP IT)


# def invertTree(self, root):
#     if root is None:
#         return None

#     # Recursively invert children *first*
#     left = self.invertTree(root.left)
#     right = self.invertTree(root.right)

#     # Then swap them
#     root.left = right
#     root.right = left

#     return root
