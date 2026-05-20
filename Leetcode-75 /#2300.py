class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(spells)
        m = len(potions)
        result = []
        for spell in spells:
            if spell >= success:
                result.append(m)
                continue
            low = 0
            high = m - 1

            while low <= high:
                mid = (low + high)//2
                if potions[mid]*spell >= success:
                    high = mid - 1
                else:
                    low = mid + 1

            result.append(m - low)

        return result
