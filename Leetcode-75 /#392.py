class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        nt = len(t)
        i = 0 
        j = 0
        while i < n and j < nt:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n

        # -- Such a Naive brute Force!!! but 100% beats :) --
        # res = []
        # n = len(s)
        # nt = len(t)
        # if n == nt: 
        #     return s == t
        # if n == 1:
        #     return s in t
        # if s == t or s == "": 
        #     return True
        # if t == "":
        #     return False
        # j = 0
        # for i in range(0, n):
        #     val = s[i]
        #     if val not in t:
        #         return False
        #     while j < len(t):
        #         if val == t[j]:
        #             res.append(j)
        #             j = j + 1
        #             break
        #         j = j + 1
        # if len(res) != n:
        #     return False
        # for j in range(1, len(res)):
        #     if res[j-1] >= res[j]:
        #         return False
        # return True
