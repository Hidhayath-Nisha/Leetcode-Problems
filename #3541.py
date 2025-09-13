class Solution:
    def maxFreqSum(self, s: str) -> int:
        counter = Counter(s)
        vowels = ["a","e", "i", "o", "u"]
        vsum = 0
        csum = 0
        for vowel in vowels:
            if vowel in counter:
                if vsum < counter[vowel]:
                    vsum = counter[vowel]
                counter.pop(vowel)
        csum = max(counter.values()) if counter else 0
        return vsum + csum
