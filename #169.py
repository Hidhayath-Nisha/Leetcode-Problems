# from collections import Counter 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)//2
        # -- Using Hash --
        # counter = Counter(nums)
        # for n in counter:
        #     if counter[n] > l:
        #         return n
        n = set(nums)
        for i in n:
            if nums.count(i) > l:
                return i
