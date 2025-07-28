# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]


# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(5)
node5 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


class Solution:
    def removeNthFromEnd(self, head, n):
        current_node = head
        len = 0

        while current_node:
            len += 1
            current_node = current_node.next

        target = len - n
        dummy = ListNode(0)
        dummy.next = head
        current_node = dummy
        for i in range(target):
            current_node = current_node.next
        current_node.next = current_node.next.next
        return dummy.next


a = Solution()
a.removeNthFromEnd(node1, 2)
