class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # -- Typical Brute Force -- 
        folder = sorted(folder)
        output = [folder[0]]
        for i in range(1, len(folder)):
            if not folder[i].startswith(output[-1] + '/'):
                output.append(folder[i])
        return output
