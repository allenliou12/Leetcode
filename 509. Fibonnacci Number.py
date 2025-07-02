# # 509. Fibonacci Number
# # Least efficient solution
# # Time complexity: O(n2)
# # Because everytime for each n, the solution will need to run again to get n
# # class Solution:
# #     def fib(self, n: int) -> int:
# #         # Base case
# #         if n == 0:
# #             return 0

# #         if n == 1:
# #             return 1

# #         else:
# #             n = self.fib(n-1) + self.fib(n-2)
# #             return n


# # More elegant method, storing the calculated number in a dict first, and check the dict first before calculating
# class Solution:
#     def __init__(self) -> None:
#         self.mem = {}

#     def fib(self, n: int) -> int:
#         if n <= 1:
#             return n
#         if n in self.mem:
#             return self.mem[n]
#         else:
#             self.mem[n] = self.fib(n-1) + self.fib(n-2)
#             return self.mem[n]


# a = Solution()
# print(a.fib(300))
