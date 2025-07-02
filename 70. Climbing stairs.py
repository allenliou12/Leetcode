# # 70. Climbing stairs
# # n = 2
# # Output: 2
# # Explanation: There are two ways to climb to the top.
# # 1. 1 step + 1 step
# # 2. 2 steps

# # Example 2:
# # Input: n = 3
# # Output: 3
# # Explanation: There are three ways to climb to the top.
# # 1. 1 step + 1 step + 1 step
# # 2. 1 step + 2 steps
# # 3. 2 steps + 1 step

# # Explanation in my own words:
# # Intuition is to not count the variations, that will only make u more confused
# # So first step is to get the base case, which in this case, is when the size of the stair(n) is 1, the only distinct way is 1
# # Second base case is that, when the size of stair is 2, the way to go up is 2 way, the reason that this is also considered a base case is because you can't break it down any further.

# # Ok since we have a constraint where we can take only either 1 or 2 steps, we know that no matter the height of stairs(n), there can only be 2 scenario:
# # Scenario 1: We take one step, and we have the remaining steps to care about
# # Scenario 2: We take two step , same as scenario one

# # Lets say we take n =3
# # Scenario 1: We take 1 step, there are 2 steps left
# # We know that there are 2 different ways to go up a stair with n height
# # Scenario 2: We take 2 step, there is only 1 step left
# # Here again we know that for a stair with height 1, there is only one way to go up
# # So we can say that the total way of distinct way to go up a height 3 stair is 3 (3+2), which is proved to be right in the example given

# # So we noticed a pattern, for stair with height 3, the correct answer is the answer of height(2) + height(1), which turn into code, height(n) = height(n-1) + height(n-2)


# class Solution:
#     def __init__(self):
#         self.mem = {}

#     def climbStairs(self, n: int) -> int:

#         if n in self.mem:
#             return self.mem[n]
#         # Base case:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         else:
#             self.mem[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
#             return self.mem[n]


# a = Solution()
# print(a.climbStairs(99))
