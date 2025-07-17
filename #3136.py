import re
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) > 2 and re.fullmatch(r'[A-Za-z0-9]+', word) and re.search(r'[aeiouAEIOU]', word) and re.search(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', word):
                return True
        return False
