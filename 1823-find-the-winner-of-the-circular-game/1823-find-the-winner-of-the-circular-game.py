class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        
        for i in range(1, n+1):
            arr.append(i)
        
        s = 0
        while len(arr) > 1:
            s = (s+k-1) % n
            arr.pop(s)
            n -= 1
                
        return arr[0]