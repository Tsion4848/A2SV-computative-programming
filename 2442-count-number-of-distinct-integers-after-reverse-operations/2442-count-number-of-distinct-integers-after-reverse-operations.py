class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        i = 0
        defined = nums[:]
        while i < len(nums):
            if nums[i] >= 0 and nums[i] < 10:
                defined.append(nums[i])
            elif nums[i] > 9:
                rev = 0
                while nums[i] > 0:
                    rem = nums[i] % 10
                    rev = (rev * 10) + rem
                    nums[i] = nums[i] // 10
                defined.append(rev)                
            i += 1
        defined = list(dict.fromkeys(defined))
        return len(defined)