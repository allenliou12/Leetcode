# # 20 Valid Parentheses

# valid = {"(": ")", "[": "]", "{": "}"}
# s = "{}]"
# stack = []
# # Output: true
# for i in s:
#     if i in valid:
#         stack.append(i)
#     # What the following line of code means is that else if the length of the stack is 0 or the value to valid[stack[-1]] is not equals to i, then print(False)
#     # Key note: the pop() method actually returns the value it is popping, so it can be directly used as the key
#     elif len(stack) == 0 or valid[stack.pop()] != i:
#         print(False)

# print(len(stack) == 0)
