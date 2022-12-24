from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # # letter = []
        # c = Counter(t)
        # print(c)
        # # key=list(c.keys())
        # # val=list(c.values())
        # # ind=val.index(c)
        # # print(key[ind])
        # for i in t:
        #     if c[i] == 1:
        #         if i not in s:
        #             return i
        #     elif c[i] > 1:
        #         if i not in s:
        #             return i
        #         elif i in s:
        #             return i
        
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
            