# The Tribonacci sequence Tn is defined as follows:

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.
# So this is an extend on the fibonacci question

# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:
# Input: n = 25
# Output: 1389537


# So like any recursion it needs a base case
# so it would be like if n is 0 it will always be 0
# 2nd is that if n is 1, then it will always be one
# 3rd case is that if n is 2, it will be one too

# so meaning starting from 4, it will do something recursively
# so n4 = n3 + n2 +n1, which we can get a general formula, n = n-1 + n-2 + n-3


# class Solution:
#     def tribonacci(self, n: int) -> int:
#         # Base case
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         if n == 2:
#             return 1

#         # Recursive case
#         count = self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
#         return count


# So the one above is the slowest algo, since everytime the number n needs to be counted again, so this would be a time complexity of O(n3) for this tribonacci question I think

# So the intuition is that we can just store the calculated solution somewhere, so that it does not need to go down on the root all over again

# So the intuition is that for every time a new number n is calculated, we store that in a dict, and in every loop? Recursion we check; If the number is already seen, we just take the stored output

class Solution:
    def __init__(self) -> None:
        self.seen = {}

    def tribonacci(self, n: int) -> int:

        # Base case
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n in self.seen:
            return self.seen[n]

        # Recursive case
        self.seen[n] = self.tribonacci(
            n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)

        return self.seen[n]


# Or even better, we dont need to init another variable?
# We can just use a helper function


class Solution:
    def tribonacci(self, n: int) -> int:
        seen = {}

        def helper(n):
            # Base case
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            if n in seen:
                return seen[n]

            # Recursive case
            seen[n] = helper(n-1)+helper(n-2)+helper(n-3)

            return seen[n]

        return helper(n)


a = Solution()
print(a.tribonacci(31))
