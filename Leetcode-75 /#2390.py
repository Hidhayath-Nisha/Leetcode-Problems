class Solution:
    def removeStars(self, s: str) -> str:
        array = []
        for i in s:
            if i == '*':
                array.pop()
            else:
                array.append(i)
        return ''.join(array)
