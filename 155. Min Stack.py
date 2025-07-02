# # 155. Min Stack
# class MinStack:

#     def __init__(self):
#         # We have two stacks here, one to hold all the stacks, and another to hold the minimum value of the added value
#         self.stack = []
#         self.min_stack = []

# # By not using the min() method, we can ensure the time complexity of the getMin() function is O(1)
#     def push(self, val: int) -> None:
#         # First we append the value to our stack
#         self.stack.append(val)
#         # Then we check, if the min_stack stack is empty or the value of val is smaller or = to the min_stack[-1], only then we append it to the min_stack stack
#         # The reason we check if the min_stack stack is empty or not first is because if we want to compare the values, we need to have at least something in the stack first, so initially the smaller value of the min_stack is going to be the 1st value added into the stack
#         if self.min_stack == [] or val <= self.min_stack[-1]:
#             self.min_stack.append(val)

#     def pop(self) -> None:
#         val = self.stack.pop()
#         if self.min_stack[-1] == val:
#             self.min_stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min_stack[-1]
