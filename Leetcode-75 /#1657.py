from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        s1 = set(word1)
        s2 = set(word2)
        if s1 != s2:
            return False
        c1 = Counter(word1)
        c2 = Counter(word2)
        return c1.values() == c2.values()
