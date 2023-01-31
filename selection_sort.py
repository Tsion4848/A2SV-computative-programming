#User function Template for python3

class Solution: 
    def select(self, arr, i):
        elem = arr[1] 
        for i in range(len(n) - 1):
            if arr[i] < arr [i + 1]:
                elem = arr[i]
        return elem
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
