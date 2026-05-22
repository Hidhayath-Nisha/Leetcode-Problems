class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # -- Naive Brute -- O(n^3)
        n = len(A)
        # result = []
        # for i in range(0, n):
        #     count = 0 
        #     for j in range(0, i+1):
        #         if B[j] in A[0:i+1]:
        #             count += 1 
        #     result.append(count)
        # return result
        

        # -- Optimal -- 
        result = [0] * n
        counterB = {}
        counterA = {}
        
        for idx,b in enumerate(B): 
            counterB[b] = idx
        for idx,a in enumerate(A): 
            counterA[a] = idx

        for idx in range(0,n-1):
            if counterB[A[idx]] <= idx:
                result[idx] += 1
            if A[idx] != B[idx] and counterA[B[idx]] <= idx:
                result[idx] += 1
            if idx != 0:
                result[idx] += result[idx-1] 

        result[n-1] = n
        return result
