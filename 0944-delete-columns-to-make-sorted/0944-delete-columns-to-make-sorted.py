class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        
        # zipped = zip(*strs)
        for row in range(len(strs[0])):
            for col in range(len(strs) - 1):
                if strs[col][row] > strs[col+1][row]:
                    count += 1
                    break
        return count
            