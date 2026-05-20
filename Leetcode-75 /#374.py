# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        myChoice = (low + high) // 2

        while guess(myChoice) != 0:
            res = guess(myChoice)
            if res == -1:
                high = myChoice - 1
            else:
                low = myChoice + 1
            myChoice = (low + high) // 2

        return myChoice
