from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        # -- Brute Force --
        for row in grid:
            for col in zip(*grid):
                if row == list(col):
                    count = count + 1
        return count

        # -- This wont be working for ordered cases--
        # def ordered_hash(arr):
        #     d = {}
        #     for x in arr:
        #         if x not in d:
        #             d[x] = 1
        #         else:
        #             d[x] += 1
        #     return d
        # count = 0
        # rowCounter = [ordered_hash(row) for row in grid]
        # colCounter = [ordered_hash(row) for row in zip(*grid)]
        # print(rowCounter, colCounter)
        # for row in rowCounter:
        #     for col in colCounter:
        #         print(row, col)
        #         if list(row.keys()) != list(col.keys()):
        #             continue
        #         rowKeys = list(row.keys())
        #         colKeys = list(col.keys())
        #         print(rowKeys, colKeys)
        #         for i in range(len(rowKeys)):
        #             if rowKeys[i] == colKeys[i] and row[rowKeys[i]] == col[colKeys[i]]:
        #                 # print(rowKeys[i], colKeys[i], row[rowKeys[i]], col[colKeys[i]])
        #                 if i == len(rowKeys) - 1:
        #                     count = count + 1 
        # return count
