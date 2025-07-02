# 739. Daily Temperatures
# temps = [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1,1,4,2,1,1,0,0]

# Note to self: I noticed a pattern when attempting the leetcode, its usually better to think of how you can get the answers first, then work backwards on the how to get the solution. Like in wat form the answer is structured, once you get that, I feel like then working backwards is easier

# The days could be the index of that day's temp minus the last day's temp that was lower. Meaning if the temp at day 6 is higher than day 5, meaning I can get the index for day 6[5] minus the index for day5[4] and i will get 1, which I can then store in the days array

# Loop through the temp
# Initialized the increasing stack with temp[0]
# If starting from temp[1] the temp is higher than the last element in the increasing stack, pop the last smallest temp from the increasing stack and append the now largest temp into the increasing stack
# If smaller, append it into the decreasing stack
# Keep comparing until the next temp[i] is larger that the stack[-1] and repeat

# for each number in temp, check if it is larger than the last number, if yes add 1 into the days array, if not
# so i think its a while loop nested inside a for loop?
# For each number, find the next number that is bigger than it, only stop when there is a bigger number than it or there is NONE
# Keep a count everytime there is no bigger number than it? or we add the smaller number into a stack? and then count that stack?

# # Populate the days output array first with empty values (0)
# days = [0] * len(temps)

# stack = []  # The stack is to store the index pointing to the temp, not the temp itselfs
# for i in range(len(temps)):
#     while stack and temps[i] > temps[stack[-1]]:
#         last_temp_index = stack.pop()
#         days[last_temp_index] = (i - last_temp_index)
#     stack.append(i)


# print(days)
