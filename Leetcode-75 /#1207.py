# -- Hash Map --
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        for i in counter:
            for j in counter:
                if i == j:
                    continue
                if counter[i] == counter[j]:
                    return False
        return True
