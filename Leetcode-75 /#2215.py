from collections import Counter
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # -- Brute Force --
        # r1 = []
        # r2 = []
        # n1 = set(nums1)
        # n2 = set(nums2)
        # for i in n1:
        #     print(i)
        #     if i in n2:
        #         continue
        #     r1.append(i) 
        # for j in n2:
        #     if j in n1:
        #         continue
        #     r2.append(j)
        # return [r1, r2]

        # -- Python Builtins --
        set1 = set(nums1)
        set2 = set(nums2)
        r1 = list(set1.difference(set2))
        r2 = list(set2.difference(set1))
        return [r1, r2]
