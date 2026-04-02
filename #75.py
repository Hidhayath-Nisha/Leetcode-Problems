class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # NOT SINGLE PASS - Brute Froce
        n = len(nums)
        # i = 0 
        # j = n - 1
        # while i<j:
        #     while j>i:
        #         if nums[i] > nums[j]:
        #             nums[j], nums[i] = nums[i], nums[j]
        #         j = j - 1
        #     i += 1
        #     j = n - 1
        # print(nums)

        # SINGLE PASS - IMMA TRY
        low = 0
        mid = 0
        high = n - 1
        while high >= mid:
            if nums[mid] == 0:
                nums[mid] = nums[low]
                nums[low] = 0
                low += 1
                mid +=1
            elif nums[mid] == 2:
                nums[mid] = nums[high]
                nums[high] = 2
                high -= 1
            else:
                mid += 1         



            
