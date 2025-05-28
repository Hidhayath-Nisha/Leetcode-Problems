class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # n = len(nums)
        # -- Brute Force --
        # for i in range(0, n ):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if nums[i] < nums[j] and nums[j] < nums[k]:
        #                 return True
        # return False    
        # -- Greedy --
        firstNum = float('inf')
        secondNum = float('inf')
        for num in nums:
            if num < firstNum:
                firstNum = num
            if num < secondNum and num > firstNum:
                secondNum = num
            if num > secondNum:
                return True
        return False
