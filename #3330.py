class Solution:
    def possibleStringCount(self, word: str) -> int:
        # -- Basic Brute Force --
        i = 0 
        j = 1
        n = len(word)
        count = 0
        while i < n:
            if j < n and word[j] == word[i]:
                j += 1
            else: 
                if j - 1 - i >= 1:
                    count +=  j - i - 1
                i = j
                j = i + 1
        return count + 1
