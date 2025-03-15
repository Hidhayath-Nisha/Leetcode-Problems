class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # -- High Beats --
        result = []
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1, n2)
        for i in range(0, n):
            result.append(word1[i])
            result.append(word2[i])
        if n1 == n2:
            return "".join(result)
        elif n1> n2:
            result.append(word1[i+1:n1])
        else:
            result.append(word2[i+1:n2])
        return "".join(result)

        # -- Using Python Built in --
        # result = []
        # n1 = len(word1)
        # n2 = len(word2)
        # n = min(n1, n2)
        # for i in range(0, n):
        #     result.append(word1[i])
        #     result.append(word2[i])
        # result.extend(word1[i+1::])
        # result.extend(word2[i+1::])
        # return "".join(result)

        # -- Two Pointer --
        # l1 = 0
        # l2 = 0 
        # n1 = len(word1)
        # n2 = len(word2)
        # result = ""
        # while l1 < n1 or l2 < n2:
        #     if l1 < n1:
        #         result = result + word1[l1] # Concatenation
        #         l1 += 1
        #     if l2 < n2:
        #         result = result + word2[l2] # Concatenation
        #         l2 += 1
        # return result
