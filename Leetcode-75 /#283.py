class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # -- Two pointers --
        i = 0
        j = 1
        n = len(nums)
        if n == 1:
            return nums
        while i < n-1:
            if nums[i]!=0:
                i = i + 1
                j = j + 1
                continue
            while j <= n - 1:
                if nums[j] != 0:
                    nums[j], nums[i] = nums[i], nums[j]
                    j = j + 1
                    break
                j = j + 1
            i = i + 1
        # -- Python Builtins --
        # count = nums.count(0)
        # for i in range(count):
        #     nums.remove(index(0))
        #     nums.append(0)
        # print(nums)
