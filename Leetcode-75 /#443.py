class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1: 
            return n
        i = 0
        j = 0
        k = 0
        while i < n:
            j = i + 1
            while j < n and chars[j] == chars[i]:
                j += 1
            chars[k] = chars[i]
            k +=1
            count = j - i
            if count > 1:
                for v in str(count):
                    chars[k] = v
                    k += 1
            i = j
        return k
