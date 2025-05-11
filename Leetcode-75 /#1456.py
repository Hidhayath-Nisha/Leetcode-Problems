class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # -- Brute Force --
        # Loop - split the array in k size - loop again and each word should be in vowels plus one else skip 
        # Two pointers and sliding windoW
        window = s[:k]
        windowCount = window.count('a') + window.count('e') + window.count('i') + window.count('o') + window.count('u')
        maxCount = windowCount
        for i in range(k,len(s)):
            if s[i-k] in ['a','e','i','o','u']:
                windowCount = windowCount - 1
            if s[i] in ['a','e','i','o','u']:
                windowCount += 1
            if maxCount < windowCount:
                maxCount = windowCount
        return maxCount
