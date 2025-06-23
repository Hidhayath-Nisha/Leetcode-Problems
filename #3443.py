class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x, y = 0, 0
        ans = 0
        for i in range(len(s)):
            if s[i] == "N":
                y += 1
            elif s[i] == "S":
                y -= 1
            elif s[i] == "E":
                x += 1
            elif s[i] == "W":
                x -= 1
            dist = abs(x) + abs(y) + k * 2
            ans = max(ans, min(dist, i + 1))
        return ans
