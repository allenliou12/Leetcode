# from collections import Counter
# nums = [4, 5, 6]
# target = 10

# arr = []
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if arr == [] and nums[i] + nums[j] == target:
#             arr.append(i)
#             arr.append(j)
#             break

#     if arr != []:
#         break


# Dictionary version
# seen = {}

# for i in range(len(nums)):
#     g = target - nums[i]
#     if g in seen:
#         print([seen[g], i])
#     else:
#         seen[nums[i]] = i


# rewrite in two pointer
# x, y = 0, len(numbers) - 1

# while x < len(numbers) and y < len(numbers):
#     if numbers[x] + numbers[y] == target:
#         print([x+1, y+1])
#         break
#     elif numbers[x] + numbers[y] > target:
#         y -= 1
#     elif numbers[x] + numbers[y] < target:
#         x += 1