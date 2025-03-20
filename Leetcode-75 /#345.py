# -- Basic Brute Force Approach --
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        j = len(s) - 1
        i = 0
        s = list(s)
        while i < j:
            if s[i] in vowels: 
                while j > i:
                    if s[j] in vowels:
                        if s[i] == s[j]:
                            j = j - 1
                            break
                        else:
                            temp = s[j]
                            s[j] = s[i]
                            s[i] = temp
                            j = j - 1
                            break
                    j = j - 1
            i = i + 1     
        return "".join(s)
