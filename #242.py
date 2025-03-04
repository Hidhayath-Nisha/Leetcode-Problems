class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #---Simple one---
        p = set(s)
        q = set(t)
        s_dict = {char: s.count(char) for char in p}
        t_dict = {char: t.count(char) for char in q}
        return s_dict == t_dict

        #---Brute Force---
        # if len(s) != len(t):
        #     return False
        # for ch in s:
        #     if s.count(ch) != t.count(ch):
        #         return False
        # return True

        #----Freq Count and Hash - Unoptimised----
        # s_dict = {}
        # t_dict = {}
        # validated = {char: False for char in s}
        # for ch in s: 
        #     if validated[ch]: 
        #         s_dict[ch] += 1
        #     else:
        #         s_dict.update({ch: 1})
        #         validated[ch] = True
        # validated = {char: False for char in t}
        # for ch in t: 
        #     if validated[ch]: 
        #         t_dict[ch] += 1
        #     else:
        #         t_dict.update({ch: 1})
        #         validated[ch] = True
        # return s_dict == t_dict

        #----Freq Count and Hash - lil Optimised----
        # s_dict = {}
        # t_dict = {}
        # for ch in s: 
        #     if ch in s_dict: 
        #         s_dict[ch] += 1
        #     else:
        #         s_dict[ch] = 1
        # for ch in t: 
        #     if ch in t_dict: 
        #         t_dict[ch] += 1
        #     else:
        #         t_dict[ch] = 1
        # return s_dict == t_dict

       

