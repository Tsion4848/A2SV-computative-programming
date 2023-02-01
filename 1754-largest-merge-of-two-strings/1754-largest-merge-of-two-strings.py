class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        length1 = len(word1)
        length2 = len(word2)
        merge = ""
        
        ptr1 = 0
        ptr2 = 0
        
        while ptr1 < length1 and ptr2 < length2:
            if word1[ptr1] > word2[ptr2]:
                merge += word1[ptr1]
                ptr1 += 1
                
            elif word1[ptr1] < word2[ptr2]:
                merge += word2[ptr2]
                ptr2 += 1
                
            else:
                p1 = ptr1 + 1
                p2 = ptr2 + 1
                
                while p1 < length1 and p2 < length2:
                    if word1[p1] > word2[p2]:
                        merge += word1[ptr1]
                        ptr1 += 1
                        break
                    elif word2[p2] > word1[p1]:
                        merge += word2[ptr2]
                        ptr2 += 1
                        break
                    else:
                        p1 += 1
                        p2 += 1
                if p1 == length1:
                    merge += word2[ptr2]
                    ptr2 += 1
                elif p2 == length2:
                    merge += word1[ptr1]
                    ptr1 += 1
                    
            if ptr1 == length1:
                merge += word2[ptr2:]
            elif ptr2 == length2:
                merge += word1[ptr1:]
                    
        return merge
