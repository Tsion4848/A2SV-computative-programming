class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        length = len(nums)
        count = 0
        
        if length < 2:
            return length
        
        while right < length:
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1
        
        return left + 1