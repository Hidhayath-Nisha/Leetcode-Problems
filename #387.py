from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        #--Brute Force--
        # hashMap = {}
        # for i,ch in enumerate(s):
        #         if ch not in hashMap:
        #             hashMap[ch] = 1
        #         else:
        #             hashMap[ch] = hashMap[ch] + 1
        # for i in hashMap:
        #     if hashMap[i] == 1:
        #         return s.index(i)
        # return -1
        counter = Counter(s)
        for i in counter:
            if counter[i] == 1:
                return s.index(i)
        return -1
