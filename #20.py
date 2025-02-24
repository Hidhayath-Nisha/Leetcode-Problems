class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        myDict = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        if not s or len(s) == 1:
            return False
        for ch in s:
            if ch == '{' or ch == '(' or ch == '[':
                myStack.append(ch)
            else: 
                if myStack:
                    if myDict[ch] == myStack.pop():
                        continue
                return False
        return True if not myStack else False
