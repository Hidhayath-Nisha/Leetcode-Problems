class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        hashMap = {
            "--X" : -1,
            "X--" : -1,
            "X++" : 1,
            "++X" : 1
        }
        x = 0
        for i in operations:
            x = x + hashMap[i]
        return x 
