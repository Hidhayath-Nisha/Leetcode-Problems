class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visitedNodes = {0}
        keyFound = [i for i in rooms[0]]
        i = 0
        while i < len(keyFound):
            if keyFound[i] in visitedNodes:
                i += 1
                continue
            else:
                for k in rooms[keyFound[i]]:
                    if k not in keyFound:
                        keyFound.append(k)
                visitedNodes.add(keyFound[i])
                i = i+1
        return len(visitedNodes) == len(rooms)
