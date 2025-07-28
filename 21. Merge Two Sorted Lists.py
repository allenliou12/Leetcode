# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]


# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

sec_node_1 = ListNode(1)
sec_node_2 = ListNode(2)
sec_node_3 = ListNode(4)

node1.next = node2
node2.next = node3

sec_node_1.next = sec_node_2
sec_node_2.next = sec_node_3




class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        p1, p2 = list1, list2

        dummy = ListNode()
        tail = dummy
        while p1 and p2:
            if p2.val > p1.val:
                tail.next = p1
                tail = tail.next
                p1 = p1.next
            else:
                tail.next = p2
                tail = tail.next
                p2 = p2.next

        if p2:
            tail.next = p2
        else:
            tail.next = p1

        return dummy.next
