class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if 1 not in nums:
            return k
        i = 0
        counter = 0
        maxValue = 0
        for j in range(0, len(nums)):
            if nums[j]==0:
                counter +=1
            while(counter > k):
                if(nums[i] == 0):
                    counter -= 1
                i += 1
            # maxValue = max(maxValue, j-i+1)
            if maxValue < j-i+1:
                maxValue = j-i+1
        return maxValue
