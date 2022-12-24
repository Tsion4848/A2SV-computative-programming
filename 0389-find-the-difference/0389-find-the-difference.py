from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:        
        ct = Counter(t)
        cs = Counter(s)
        print(ct)
        print(cs)
        
        for i in t:
            if i not in s:
                return i
            if i in s:
                if ct[i] == cs[i] + 1:
                    return i
            
