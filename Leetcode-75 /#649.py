class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dQ = []
        rQ = []
        n = len(senate)
        for i in range(n):
            if senate[i] == 'R':
                rQ.append(i)
            else:
                dQ.append(i)
        while rQ and dQ: # If both the queues aren't empty
            r = rQ.pop(0)
            d = dQ.pop(0)
            if r < d:
                rQ.append(r+n)
            else:
                dQ.append(d+n)
        return "Dire" if dQ else "Radiant"
