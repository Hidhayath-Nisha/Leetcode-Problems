class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = n+m-1
        while i > -1 and j > -1:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        if j < 0:
            return nums1
        while j > -1:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        return nums1
