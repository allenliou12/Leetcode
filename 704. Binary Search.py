# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Start from the middle of the array, if the number at position n(the middle of array) is larger than target,  then repeat the same step for the left half until you get the target.
# Need to figure out how to get the index, maybe can use the .index() ? Since the time complexity is O(1),

# Wrong idea
# class Solution:
#     def search(self, nums, target: int) -> int:
#         mid = int(len(nums)/2)
#         left = nums[0:mid]
#         right = nums[mid::]
#         if target not in nums:
#             return -1
#         if nums[mid] == target:
#             return mid
#         if nums[mid] > target:
#             nums = left
#             return self.search(nums, target)
#         else:
#             nums = right
#             return self.search(nums, target)

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Start from the middle of the array, if the number at position n(the middle of array) is larger than target,  then repeat the same step for the left half until you get the target.
# Need to figure out how to get the index, maybe can use the .index() ? Since the time complexity is O(1),


# Ok so this way uses a helper function, the first idea of mine was almost correct, take the middle of the array, then recursively check if the number at index middle is the target or not

# So the whole recursive case is that, if the num at mid is higher than the target, that means the number is somewhere at from the index 0  up til the index mid of the array, so we remain the low to be 0, and set the high of the number we can to check to be mid -1. (The reason we take mid -1 and not just mid is bcos we already checked the number at index mid, we want to check the last number before index mid)
class Solution:
    def search(self, nums, target: int) -> int:
        def bin_search(low, high):
            mid = (low + high) // 2

            if low > high:
                return -1

            if nums[mid] == target:
                return mid

            else:
                if nums[mid] > target:
                    high = mid - 1
                    return bin_search(low, high)
                elif nums[mid] < target:
                    low = mid + 1
                    return bin_search(low, high)

        return bin_search(0, len(nums)-1)


nums = [-1, 0, 7, 9, 11, 12]
target = 9
a = Solution()
print(a.search(nums, target))
