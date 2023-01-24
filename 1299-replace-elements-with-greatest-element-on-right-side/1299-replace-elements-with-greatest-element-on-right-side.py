class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # last = len(arr) - 1
        # # while arr[last] != -1:
        # for num in range(last):
        #     maxim = max(arr[num+1:])
        #     arr[num] = maxim
        #     print(arr[num])
        # arr[last] = -1
        # print(arr[last])
        # return arr
        maxRight = -1
        for num in reversed(range(len(arr))):
            arr[num], maxRight = maxRight, max(maxRight, arr[num])
        return arr