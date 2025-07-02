# # 150. Evaluate Reverse Polish Notation
# # Output: 9  ((2 + 1) * 3) = 9
# import operator
# tokens = ["4", "13", "5", "/", "+"]
# # Use a stack method?
# # Basically, add in the int to stacks until u reach an operator then for the two previous int behind the operator do that using the operator then continue to the end of the tokens
# operators = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv
# }


# class Solution:
#     def evalRPN(self, tokens) -> int:
#         operators = {
#             "+": operator.add,
#             "-": operator.sub,
#             "*": operator.mul,
#             "/": operator.truediv,
#         }

#         stack = []
#         for i in range(len(tokens)):
#             try:
#                 int(tokens[i])
#                 stack.append(int(tokens[i]))
#             except ValueError:
#                 r_num = stack.pop()
#                 l_num = stack.pop()
#                 stack.append(operators[tokens[i]](l_num, r_num))
#         return ((stack[-1]))


# a = Solution()

# print(a.evalRPN(tokens))
