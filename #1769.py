class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # -- Brute Force --
        n = len(boxes)
        arr = [0] * n
        for i in range(0, n):
            for j in range(0, n):
                if boxes[j] == '1':
                    arr[i] += abs(j - i)
        return arr
