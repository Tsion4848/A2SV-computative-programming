class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ordered = []
        for i in nums:
            if i % 2 == 0:
                ordered.append(i)
        for i in nums:
            if i % 2 != 0:
                ordered.append(i)
        return ordered