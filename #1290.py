class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        array = []
        number = 0
        while head != None:
            array.append(head.val)
            head = head.next
        for idx, i in enumerate(array[::-1]):
            if i == 1:
                number += pow(2, idx)
        return number
