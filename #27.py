class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(0, len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[k] = nums[i]
                k = k + 1
        return k
