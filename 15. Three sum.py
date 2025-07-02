# nums = [-1, 0, 1, 2, -1, -4]
# nums = sorted(nums)  # [-4, -1, -1, 0, 1, 2]


# for i in range(len(nums)):
#     y = len(nums)-1
#     x = i+1
#     # To avoid duplicate, meaning if its not the first number, and that number is not equal to its previous number, continue
#     if i > 0 and nums[i] == nums[i - 1]:
#         continue
#     while x < y:

#         total = nums[i] + nums[x] + nums[y]
#         if total == 0:
#             print([nums[i], nums[x], nums[y]])
#             x += 1
#             y -= 1
#         elif total < 0:
#             x += 1
#         elif total > 0:
#             y -= 1
