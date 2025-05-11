class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = 1 if len(arr)==3 else len(arr)-2
        for i in range(0, n):
            # print(arr[i])
            if arr[i]%2 == 1 and arr[i+1]%2 == 1 and arr[i+2]%2 == 1:
                return True
        return False
