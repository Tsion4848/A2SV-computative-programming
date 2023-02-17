n, m = map(int, input().split())
arr = []
res = []

# adding to our array
for _ in range(n):
    inp = input()
    arr.append(inp)

col = [[0 for j in range(n)] for i in range(m)]
array = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        array[i][j] = arr[i][j]

for i in range(m):
    for j in range(n):
        col[i][j] = array[j][i]


for i in range(n):
    for j in range(m):
        rowC = array[i][:j] + array[i][j+1:]
        colC = col[j][:i] + col[j][i+1:]

        if arr[i][j] in rowC or arr[i][j] in colC:
            continue
        else:
            res.append(arr[i][j])

res = ''.join(res)
print(res)
