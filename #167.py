class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers) - 1
        i = 0
        while i < j: 
            value = numbers[i] + numbers[j]
            if value == target:
                return [i+1, j+1]
            if value > target:
                j = j - 1
            if value < target:
                i = i + 1
