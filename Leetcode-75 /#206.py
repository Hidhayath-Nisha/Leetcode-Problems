# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # -- Basic Brute Force --
        myArray = []
        if head == None: 
            return None
        while head:
            myArray.append(head.val)
            head = head.next
        prev = None
        for val in myArray:
            new_node = ListNode(val)
            new_node.next = prev
            prev = new_node
        return prev
