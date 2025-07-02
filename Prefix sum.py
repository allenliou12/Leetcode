# # Prefix sum
# nums = [10, 20, 10, 5, 15]

# # 1st number is always the same or in another words is 0 +10 = 10
# # starting from the 2nd number, the expected output is the addition of all previous values
# # 2nd number = 20+10 = 30
# # 3rd num = 30 +10 =40
# # Mayb I can have a number to hold the sum, starting at 0, then add in the next number when it comes to the next loop

# P_sum = 0
# arr = []
# for i in nums:
#     arr.append(P_sum + i)
#     P_sum = P_sum + i

# print(arr)
