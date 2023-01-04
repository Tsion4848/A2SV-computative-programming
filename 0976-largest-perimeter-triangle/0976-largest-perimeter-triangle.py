class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maxim = 0
        n = len(nums)
        nums.sort(reverse = True)
        
        for i in range(0, n - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                maxim = max(maxim, nums[i] + nums[i+1] + nums[i+2])
                break
        return maxim