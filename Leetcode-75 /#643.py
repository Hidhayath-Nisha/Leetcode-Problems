class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        maxSum = window
        for i in range(k, len(nums)):
            window = window - nums[i-k] + nums[i]
            maxSum = max(window, maxSum)

        return maxSum/k
