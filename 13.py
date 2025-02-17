class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        flag = [False] * len(s)
        value = { 
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for i in range(0, len(s)):
            if flag[i]:
                continue
            else:
                if i < len(s)-1 and value[s[i]] < value[s[i+1]]:
                    sum = sum + (value[s[i+1]] - value[s[i]])
                    flag[i] = True
                    flag[i+1] = True
                else:
                    sum = sum + value[s[i]]
                    flag[i] = True
        return sum
