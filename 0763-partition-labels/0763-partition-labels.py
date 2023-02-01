class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """            
        rightmostLetter = {c: i for i, c in enumerate(s)}
        l = 0
        r = 0
        res = []
        
        
        for i, c in enumerate(s):
            r = max(r, rightmostLetter[c])
            if i == r:
                res.append(r - l + 1)
                l = r + 1
        return res
        