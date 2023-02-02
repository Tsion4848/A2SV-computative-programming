class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []

        for target in range(len(arr), 0, -1):
            index = arr.index(target)
            arr[:index + 1] = arr[:index + 1][::-1]
            arr[:target] = arr[:target][::-1]
            res.append(index + 1)
            res.append(target)
            
        return res