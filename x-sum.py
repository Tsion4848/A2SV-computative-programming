from collections import defaultdict
 
testC = int(input().strip())
 
for _ in range(testC):
    n, m = map(int, input().split())
    diag = defaultdict(int)
    antiDiag = defaultdict(int)
    maxim = ind = -1
    arr = []
 
    for i in range(n):
        arrs = list(map(int, input().split()))
        arr.append(arrs)
 
    for i in range(n):
        for j in range(m):
            diag[i-j] += arr[i][j]
            antiDiag[j + i] += arr[i][j]
 
    for i in range(n):
        for j in range(m):
            maxim = max(maxim, (diag[i-j] + antiDiag[j+i] - arr[i][j]))
 
    print(maxim)
