class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        sq_n = n*n
        if n < 2 or n > 50:
            return []
        hashArray = [0 for i in range(sq_n)]
        for i in range(n):
            for j in range(n): 
                val = grid[i][j]
                if val > sq_n or val < -1:
                    return []
                else:
                    hashArray[val-1] += 1
        b = hashArray.index(0) + 1
        a = hashArray.index(2) + 1
        # for i, idx in enumerate(hashArray):
        #     if idx == 2 or idx == 0:
        #         if idx == 2:
        #             a = i+1
        #         if idx == 0:
        #             b = i+1
        #     continue
        return [a, b]


