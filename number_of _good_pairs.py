class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j:
                    if nums[i] == nums[j]:
                        count += 1
                        # print("({}, {}), ".format(i,j))
        return count               
