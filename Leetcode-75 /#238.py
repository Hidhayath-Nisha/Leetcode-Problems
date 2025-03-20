# -- Without using division operator - the concept is right elements product * left elements products --
class Solution: 
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        prefixSum = [1]* len(nums)
        for i in range(1, len(prefixSum)): 
            prefixSum[i] = nums[i-1] * prefixSum[i-1] 
        suffix = 1
        for i in range(len(prefixSum)-1, -1, -1):
            prefixSum[i] = prefixSum[i] * suffix
            suffix = suffix * nums[i]
        return prefixSum
