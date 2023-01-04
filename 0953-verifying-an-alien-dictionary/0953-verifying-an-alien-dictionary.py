class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {}
        for i, char in enumerate(order):
            dictionary[char] = i
            
        for i in range(len(words) - 1):
            curr = words[i]
            next = words[i + 1]
            for j in range(len(curr)):
                if j >= len(words[i + 1]):
                    return False
                if curr[j] != next[j]:
                    if dictionary[curr[j]] > dictionary[next[j]]:
                        return False
                    break
        return True