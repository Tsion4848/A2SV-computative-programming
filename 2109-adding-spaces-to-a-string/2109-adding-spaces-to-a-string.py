class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        ind = 0
        
        for i, c in enumerate(s):
            if ind < len(spaces) and i == spaces[ind]:
                res.append(' ')
                ind += 1
            res.append(c)
        return ''.join(res)