# 437. Path Sum III
# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
# Based on the question, I would need to use the dfs technique since I need to go through each and every tree
# The special thing is that it doesnt need to start or end at root, but only go downwards
# So from a specific node I need to keep going until the current sum is equals target?
# And whenever I match the target I increase a count by one
# So what is my base case
# 1 i could think of is if root is None, then return 0
# 2nd is that if root is target sum, return root value?
# the recursive case is this:
# root + root.left, root +root.right
# However there is a condition, if the current sum is lesser than t continue with the recursive case
# If the current sum is > t, I will need to remove the root and continue from the root.left or root.right and recursively do the addition again
# I can take inspiration from path sum II


class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return 0
        res = []

        def dfs(node, path_so_far, current_sum, count):
            if not node:
                return count
            if node == targetSum:
                path_so_far += [node]
                count += 1
            current_sum += node.val
            if current_sum == targetSum:
                path_so_far += [node.val]
                res.append(path_so_far)
            if current_sum < targetSum:
                path_so_far += [node.val]
                dfs(node.left, path_so_far, current_sum, count)
                dfs(node.right, path_so_far, current_sum, count)
            elif current_sum > targetSum:
                path_so_far.remove(node.val)
                dfs(node.left, path_so_far, current_sum, count)
                dfs(node.right, path_so_far, current_sum, count)

        dfs(root, [], 0, 0)
        return len(res)


# Guidance from GPT
#
class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return 0
        count = [0]

        def dfs_from_node(node, current_sum):
            if not node:
                return
            current_sum += node.val
            if current_sum == targetSum:
                count[0] += 1
            dfs_from_node(node.left, current_sum)
            dfs_from_node(node.right, current_sum)

        dfs_from_node(root, 0)

        return (
            count[0] +
            self.pathSum(root.left, targetSum) +
            self.pathSum(root.right, targetSum)
        )
