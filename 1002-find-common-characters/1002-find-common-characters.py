class Solution:
    from collections import Counter
    def commonChars(self, words: List[str]) -> List[str]:
        
        wor = Counter(words[0])
    
        for i in words:
            rest = Counter(i)
            
            for j in wor:
                wor[j] = min(wor[j], rest[j])
        print(wor)
        
        ans = []
        
        for i in wor:
            for j in range(wor[i]):
                ans.append(i)
        return ans
            
       
      