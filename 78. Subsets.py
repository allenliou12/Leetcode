# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
nums = [1, 2, 3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]


# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

# Mayb I can solve this recursively?
# So no matter how long nums is, I can confirm that there are 3 subsets: The  empty array and each element of the array and the entire array
# So the if the num is empty: return empty array
# If len= 1" subset = [[],[n1]]
# if len >1:
# for each element:
# 1st return that element
# then return an array of that element and its next element
# Then return an array of that element and its last next element +1, all the way until the end of the array, then remove the 1st element in the array


class Solution:
    def subsets(self, nums):
        ss = []

        def bt(start, path):
            for i in range(start, path):
                pass
                # Leave until another day
