class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = len(a)
        n2 = len(b)
        n1Sum, n2Sum = 0, 0

        p = 0
        for i in range(n1-1, -1, -1):
            n1Sum = n1Sum + (int(a[i]) * (2**p))
            p += 1

        p = 0
        for i in range(n2-1, -1, -1):
            n2Sum = n2Sum + (int(b[i]) * (2**p))
            p += 1

        dec = n1Sum + n2Sum

        if dec == 0:
            return "0"

        res = []
        while dec != 0:
            res.append(str(dec % 2))
            dec = dec // 2

        return "".join(res[::-1])
