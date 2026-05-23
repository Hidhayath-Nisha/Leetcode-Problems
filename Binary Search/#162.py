class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        # if n == 2:
        #     return 0 if nums[0] > nums[1] else 1
        left = 0 
        right = n - 1

        while left< right:
            mid = (left + right)//2

            # if mid == 0:
            #     return mid+1 if nums[0] < nums[1] else mid
            # if mid == n-1:
            #     return mid if nums[mid] > nums[mid - 1] else mid - 1
            # if nums[mid+1] < nums[mid] > nums[mid-1]:
            #     return mid
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid

        return left
