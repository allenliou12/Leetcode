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
node3 = ListNode(3)


node1.next = node2
node2.next = node3


class Solution:
    def reverseList(self, head):
        current_node = head
        # Base case if we are at the end of the LL, just return the current node
        if head is None or current_node.next is None:
            return current_node

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head


sol = Solution()
reversed_head = sol.reverseList(node1)
