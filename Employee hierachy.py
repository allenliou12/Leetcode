# DFS for employeee hierachy
# class Employee:
#     def __init__(self, name):
#         self.name = name
#         self.subordinates = []

#     def add_subordinate(self, emp):
#         self.subordinates.append(emp)

#     def get_all_subordinates(self):
#         result = []

#         def dfs(employee):
#             for sub in employee.subordinates:
#                 result.append(sub.name)
#                 dfs(sub)

#         dfs(self)
#         return result


# # Create all employee objects
# employees = {}
# names = ["ceo", "e1", "e2", "e3", "e4", "e5", "e6"]
# for name in names:
#     employees[name] = Employee(name)


# # Define the relationships
# relations = [
#     ("e1", "ceo"),
#     ("e2", "e1"),
#     ("e3", "e1"),
#     ("e4", "e3"),
#     ("e5", "e3"),
#     ("e6", "e5")
# ]

# # Build the hierarchy
# for emp, manager in relations:
#     employees[manager].add_subordinate(employees[emp])

# print(employees["e1"].get_all_subordinates())
