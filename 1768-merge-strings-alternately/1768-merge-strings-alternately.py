class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        word1 = [*word1]
        word2 = [*word2]
        
        min_len = min(len(word1), len(word2))
        
        ptr1 = 0
        ptr2 = 0
        
        for i in range(min_len):
            answer += word1[i]
            ptr1 += 1
            answer += word2[i]
            ptr2 += 1
            
        while ptr1 < len(word1):
            answer += word1[ptr1]
            ptr1 += 1
            
        while ptr2 < len(word2):
            answer += word2[ptr2]
            ptr2 += 1
            
        print(answer)
        return answer