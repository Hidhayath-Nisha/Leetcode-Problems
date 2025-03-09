# from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # -- Hash Method --
        # counterR = Counter(ransomNote)
        # counterM = Counter(magazine)
        # for i in counterR:
        #     if counterR[i] > counterM[i]:
        #         return False
        # return True
        # -- Optimised Solution --
        seen= set()
        for i in ransomNote:
            if i in seen:
                continue
            if ransomNote.count(i) > magazine.count(i):
                return False
            seen.add(i)
        return True
