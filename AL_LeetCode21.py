# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Check large value in l1 and l2 first and check l1 is emnpty, then check l2
        if (not l1) or (l2 and (l1.val > l2.val)):
            l1, l2 = l2, l1
        # if l1 is valid, call the function to compare the next values
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1