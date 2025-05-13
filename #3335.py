class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # -- Hash Map and unoptimised --
        hashArray = {}
        for i in range(0, len(s)):
            if s[i] not in hashArray:
                hashArray[s[i]] = 1
            else:
                hashArray[s[i]] = hashArray[s[i]] + 1
        # print(hashArray)
        ct = 0
        while ct < t:
            ct += 1
            newHash = {}
            for i in hashArray:
                if i == "z":
                    if 'a' not in newHash:
                        newHash['a'] = hashArray['z']
                    else:
                        newHash['a'] = hashArray['z'] + newHash['a']
                    if 'b' not in newHash:
                        newHash['b'] = hashArray['z']
                    else:
                        newHash['b'] += hashArray['z']
                else:
                    if chr(ord(i)+1) not in newHash:
                        newHash[chr(ord(i)+1)] = hashArray[i] 
                    else:
                        newHash[chr(ord(i)+1)] += hashArray[i]
            hashArray = newHash
            # print(hashArray)
        return sum(hashArray.values()) % (10**9 + 7)
        # -- Brute Force --
        # while ct < t:
        #     ct += 1
        #     i = 0
        #     while i < len(s):
        #         if s[i] == "z":
        #             changedCh = "ab"
        #             s = s[:i] + changedCh + s[i + 1 :]
        #             i = i + 2
        #         else:
        #             chrValue = 122 - (122 - ord(s[i])) + 1
        #             changedCh = chr(chrValue)
        #             s = s[:i] + changedCh + s[i + 1 :]
        #             i = i + 1
        # return len(s)
