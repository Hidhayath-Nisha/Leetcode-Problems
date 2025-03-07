class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashMap = {}
        for i,ch in enumerate(s):
                if ch not in hashMap:
                    hashMap[ch] = 1
                else:
                    return ch
        return -1
