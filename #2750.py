class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0 
        n1 = len(nums1)
        n2 = len(nums2)
        res = []
        while i < n1 and j < n2:
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1]])
                i = i + 1
            elif nums1[i][0] > nums2[j][0]:
                res.append([nums2[j][0], nums2[j][1]])
                j = j + 1
        if i < n1:
            for k in range(i, n1):
                res.append(nums1[k])
        if j < n2:
            for k in range(j, n2):
                res.append(nums2[k])
        return res
