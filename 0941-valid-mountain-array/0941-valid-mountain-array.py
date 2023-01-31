class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        if len(arr) < 3:
            return False

        maxim = max(arr)
        maxind = arr.index(maxim)
        
        if length - 1 == maxind or maxind == 0:
            return False
        
        left = 0
        right = maxind
        
        flag = 0
        
        while left < maxind:
            if arr[left] >= maxim or arr[left] >= arr[left + 1]:
                return False
            left += 1
        
        while right < length - 1:
            if arr[right] <= arr[right + 1]:
                return False
            right += 1
        return True
            
        # if (flag == 1):
        #     return True
        # else:
        #     return False
        
        
        
        
        # for left in range(length - 1):
        #     right = left + 1:
        #         if arr[left] > arr[right]:
        #             return 
                