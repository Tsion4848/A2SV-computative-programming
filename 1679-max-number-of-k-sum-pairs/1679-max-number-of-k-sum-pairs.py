class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        diction = defaultdict(int)
        cnt = 0 
        
        for num in nums:
            target = k - num
            
            if diction[target] > 0:
                diction[target] -= 1
                cnt += 1
            else:
                diction[num] += 1
                
        return cnt 