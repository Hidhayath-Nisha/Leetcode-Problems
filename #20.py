class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        if s.count('(') == s.count(')') and s.count('[') == s.count(']') and s.count('{') == s.count('}'):
            return True
        return False
