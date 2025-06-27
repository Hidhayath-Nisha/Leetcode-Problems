# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #--Basic Brute Force with HashMap/Set --
        seen = set()
        if head == None or head.next == None:
            return False
        if head.next == head:
            return True
        while head.next != None:
            if head.next in seen:
                return True
            else:
                seen.add(head.next)
                head = head.next

        
