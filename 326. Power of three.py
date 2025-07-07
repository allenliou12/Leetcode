# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:
# Input: n = 27
# Output: true
# Explanation: 27 = 3 power 3

# Example 2:
# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.

# Example 3:
# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).


# Intuition, check the modulo? If the number modulo 3 is 0 then its a power of Three? X this doesnt work, since 45 can be divided by 3 but is not a power of 3

# 2nd, maybe use the square root? X wrong again
# If the square root of n can be modulo 3

# 3rd, mayb using a brute force method? Correct
# while the result of 3 x3 is lesser than n, keep going? And then if the result is  == n return True?

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        else:
            res = 3
            while res < n:
                res *= 3

            return True if res == n else False


a = Solution()
print(a.isPowerOfThree(27))

# But since this is a recursion question, try a recursive way
# Ok so for recursive question we need a base case
# Nvm go back, actually all the brute force method is doing is keep multiplying the output by 3 and check if the output is == n, maybe this is the recursive case?

# The base case is that if it is lesser than 1, its not a power of 3, but for some reason 1 is a power of 3 (So the rule is that any number raised to the power of 0 is 1 so 1 is a power of any number)

# so if n =27, n is the output, we can have a variable y, so this reminds me alot of the fibonacci sequence, the y number, is actually just (y -1) *3, but how does it turn this question into a recursive though? Since what its expecting is always boolean

# Ok so the correct answer requires me to think it another way, instead of keep multiplying 3, as long as the number can be divided by 3 all the way to 1 then the n is a power of 3, since 27 (Which is a power of 3) is just 3 *3 * 3, it can also be intepreted as , 27 /3 = 9, 9/3 = 3, 3/3 =1


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1 or n % 3 != 0:
            return False

        return self.isPowerOfThree(n//3)
