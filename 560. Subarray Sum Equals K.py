# 560. Subarray Sum Equals K


# Output: 2
# 1st attempt
# Goal is to get the amount of numbers that are next to each other that adds up to k
# Remind me of the two sum problem? Using hash table to check if the number is in seen?
# for each number[i], check if number[i] + number[i+1] == k?
# Using the prefix sum method, i need to keep getting the prefix sum until it reaches k?
# Then i return the len(arr) as the answer
# c_sum = 0
# arr = []

# for i in nums:
#     if c_sum < k:
#         arr.append(c_sum + i)
#         c_sum += i

#     if c_sum == k:
#         print(len(arr))

# 2nd attempt Brute force
# Same idea using the prefix sum method
# if num is [1,2,3]
# I need to check each continuing number if it add ups to k
# First I check the 1st number if its == to k, if yes add it to an array to store it?
# NExt if i add the number 1 and its neighbour 2 i get 3, which is the k, same if it is equals to k add in the array
# Next is to check 2 and 3, which = 5, which is bigger than k,
# next check the last number which is 3, if its == k then append it into an array
# Lastly return the len of the array
# count = 0
# for i in range(len(nums)):
#     total = 0
#     for j in range(i, len(nums)):
#         total += nums[j]
#         if total == k:
#             count += 1
# print(count)

# 3rd attempt Prefix sum

# Loop through the nums
# add prefix sum to each nums and then update the new prefix sum
# If the prefix sum is lower than k, continue adding next number
# If the prefix sum is bigger, reset the prefix sum and get the i +1 number and start from there
# nums = [1]
# k = 0
# count = 0
# pref_sum = 0
# seen = {0: 1}
# for i in nums:
#     pref_sum += i
#
# Check for matches first
#     if pref_sum - k in seen:
#         count += seen[pref_sum-k]
# What this line is saying is that, if the key doesnt exist, the default value is 0, and then +1
# Then update the dictionary
#     seen[pref_sum] = seen.get(pref_sum, 0)+1
# print(count)
