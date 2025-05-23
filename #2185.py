class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            count = (count + 1) if word.startswith(pref) else count
        return count
