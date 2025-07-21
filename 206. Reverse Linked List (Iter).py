# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []


# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(1)
node2 = ListNode(2)


node1.next = node2


class Solution:
    def reverseList(self, head):
        current_node = head
        prev = None
        while current_node is not None:
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next
        return prev


# First intuition is to loop through the entire LL, until the end of the list, and set its next node to be its previous node.
a = Solution()
print(a.reverseList(node1))
