# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None or head.next == None:
            return head
        oddPrev = head
        evenPrev = head.next
        evenStart = evenPrev
        while evenPrev and evenPrev.next:
            oddPrev.next = evenPrev.next
            oddPrev = oddPrev.next
            evenPrev.next = oddPrev.next
            evenPrev = evenPrev.next
        oddPrev.next = evenStart
        return head
