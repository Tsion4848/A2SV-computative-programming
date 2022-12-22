class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        
        minimum = len(min(strs, key = len))
        print(minimum)
        ch = strs[0]
        
        for i in range(minimum):
            for j in strs:
                if j[i] != ch[i]:
                    return ch[:i]
        return ch[:minimum]
        