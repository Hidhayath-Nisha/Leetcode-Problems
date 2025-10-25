class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # hashMap = {i[0]: i[1] for i in connections}
        hashMap = defaultdict(list)
        reverseMap = defaultdict(list)
        for i in connections:
            hashMap[i[0]].append(i[1])
        # reverseMap = defaultdict(list)
        # for i in connections:
            reverseMap[i[1]].append(i[0])
        visited = set()
        array = deque([0])
        c = 0
        while array:
            parentNode = array.popleft()
            if parentNode in visited: 
                continue
            temp = []
            for child in hashMap[parentNode]:
                if child not in visited:
                    array.append(child)
                    c += 1
            # if parentNode in hashMap:
            #     array.extend(hashMap[parentNode])
            # if parentNode in reverseMap:
            #     array.extend(reverseMap[parentNode])
            for child in reverseMap[parentNode]:
                if child not in visited:
                    array.append(child)
            visited.add(parentNode)
            # for currNode in temp:
            #     if [parentNode, currNode] in connections:
            #         c += 1
        return c
