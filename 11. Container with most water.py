# Container with most water
# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# l, r = 0, len(height)-1
# area = min(height[l], height[r]) * (r - l)

# max_a = 0
# while r > l:
#     area = min(height[l], height[r]) * (r - l)
#     if area > max_a:
#         max_a = area
#     if height[l] < height[r]:
#         l += 1
#     else:
#         r -= 1

# print(max_a)
