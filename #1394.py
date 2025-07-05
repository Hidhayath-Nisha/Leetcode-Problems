class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        v = -1
        for i in counter:
            if i == counter[i] and i > v:
                v = i
        return v
