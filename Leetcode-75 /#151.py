class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split(" ")
        sList = list(filter(None, sList))
        j = len(sList) - 1
        i = 0
        while i < j:
            sList[i], sList[j] = sList[j] , sList[i]
            i = i + 1
            j = j  - 1
        print(sList)
        return " ".join(sList)
