class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # -- Two Pointers -- O(n log n) 
        # nums.sort()
        # i = 0 
        # j = len(nums)-1
        # count = 0
        # while i < j:
        #     currSum = nums[i] + nums[j]
        #     if currSum == k:
        #         count = count + 1
        #         i = i + 1
        #         j = j - 1
        #     elif currSum < k:
        #         i = i + 1
        #     else:
        #         j = j - 1
        # return count
        # -- Hashmap Approach -- 
        count = 0
        hashMap = Counter(nums)
        for x in hashMap.keys():
            if k/2 == x:
                currCount = hashMap[x]//2
                count += currCount
                hashMap[x] -= currCount
                continue
            if hashMap[k-x] != 0:
                currCount = min(hashMap[x], hashMap[k-x])
                count += currCount
                hashMap[x] -= currCount
                hashMap[k-x] -= currCount
        return count
