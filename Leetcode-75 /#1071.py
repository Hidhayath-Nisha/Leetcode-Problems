from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1 = set(str1)
        s2 = set(str2)
        if s1 != s2:
            return ""
        if str1+str2 != str2+str1:
            return ""
        n = gcd(len(str1), len(str2))
        return str1[0:n]
