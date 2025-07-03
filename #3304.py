class Solution:
    def kthCharacter(self, k: int) -> str:
        s= 'a'
        while len(s) < k:
            c = ''
            for i in s:
                if i == 'z':
                    c = c + 'a'
                else:
                    c = c + chr(ord(i) + 1)
            s = s + c
        return s[k-1]
