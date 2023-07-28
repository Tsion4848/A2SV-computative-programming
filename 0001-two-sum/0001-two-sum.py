class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis = []
#         i = 0
#         # j = len(nums) - 1

#         while i+1 < len(nums)-1:
#             val = nums[i]

#             if target - nums[i] == val:
#                 lis.append(val)
#                 lis.append(nums.index(nums[i]))
#                 return lis                

#             i += 1

        i = 0

        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    lis.append(i)
                    lis.append(j)
                    return lis
                j += 1
            i += 1