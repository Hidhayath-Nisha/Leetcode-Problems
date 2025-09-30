class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)
        for arr in trust:
            in_degree[arr[1]] += 1
            out_degree[arr[0]] -= 1
        for i in range(1, len(in_degree)):
            if in_degree[i] == n-1 and out_degree[i] == 0:
                return i
        return -1
