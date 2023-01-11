class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        #adding numbers which are even
        summ = sum(num for num in nums if num % 2 == 0)
        
        for query in queries:
            if nums[query[1]] % 2 == 0:
                summ -= nums[query[1]]
            nums[query[1]] += query[0]
            if nums[query[1]] % 2 == 0:
                summ += nums[query[1]]
            res.append(summ)
        return res