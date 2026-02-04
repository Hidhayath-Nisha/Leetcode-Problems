class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        l = len(nums)
        if l < 4: 
            return False
        p = -1
        for i in range(1, l):
            if nums[i] == nums[i-1]:
                return False
            if nums[i] > nums[i-1]:
                continue
            else:
                if i > 1:
                    p = i - 1
                    break
                else:
                    return False
        if p == -1:
            return False
        q = -1
        for i in range(p + 1, l):
            if nums[i] == nums[i-1]:
                return False
            if nums[i] < nums[i-1]:
                continue
            else:
                if i > p + 1:
                    q = i - 1
                    break
                else:
                    return False

        if q == -1:
            return False
        if not (0 < p < q < l - 1):
            return False
        if q + 1 >= l:
            return False

        for i in range(q + 1, l):
            if nums[i] == nums[i-1]:
                return False
            if nums[i] > nums[i-1]:
                continue
            else:
                return False 

        return True
