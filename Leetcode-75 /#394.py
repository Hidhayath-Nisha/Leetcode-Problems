class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        k= ''
        numbers= []
        chars = []
        for i in range(0, n):
            if s[i].isdigit():
                k = k + s[i]
                if s[i+1] == '[':
                    numbers.append(k)
                    k =''
                else:
                    continue
            elif s[i] != ']':
                chars.append(s[i])
            else: 
                ss = ''
                while len(chars) > 0:
                    v = chars.pop()
                    if v != '[':
                        ss = v + ss
                    else:
                        break
                chars.append(ss * int(numbers.pop()))
        return ''.join(chars)
