
class Solution:
    def arraySortedOrNot(self, arr, n):
        for left in range(n - 1):
            right = left + 1
            if arr[left] > arr[right]:
                return False
        return True
