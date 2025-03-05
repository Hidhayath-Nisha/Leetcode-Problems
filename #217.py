# from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = set() #stores only distinct values
        for n in nums:
            if n in distinct:
                return True
            distinct.add(n)
        return False


        #--One Liner--
        #return any(count > 1 for count in Counter(nums).values())
        
        #---- Simple Method-----
        # n = set(nums)
        # n_list = {val: nums.count(val) > 1 for val in n}
        # return True in n_list.values()

        #---Brute Force---
        # n_dict = {}
        # for val in nums:
        #     if val in n_dict:
        #         n_dict[val] = True
        #     else:
        #         n_dict[val] = False
        # return True in n_dict.values()
