class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        if len(nums) == 0:
            return
        
        res = [None] * len(nums)
        
        for i in range(len(nums)):
            newInd = (i + k) % len(nums)
            res[newInd] = nums[i]
            
        for i in range(len(nums)):
            nums[i] = res[i]
       