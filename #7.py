class Solution:
    def reverse(self, x: int) -> int:
        revNumber = 0
        flag = 1 if x < 0 else 0
        if flag:
            x = x * -1 
        while x > 0:
            lastDigit = x % 10
            x = x // 10
            revNumber = ( revNumber * 10 ) + lastDigit
        revNumber = revNumber * -1 if flag else revNumber
        if revNumber > pow(2, 31) - 1 or revNumber < pow(-2, 31):
            return 0
        return revNumber
