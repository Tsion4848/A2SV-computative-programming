# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
dict = {}
d = defaultdict(list)

n,m = map(int, input().split())
A = []
for i in range(n):
    A.append(input())
B = []
for i in range(m):
    B.append(input())
ind = 0
for i in A:
    d[i].append(A.index(i,ind)+1)
    ind += 1
for i in B:
    if i not in A:
        print(-1)
    else:
        print(" ".join(map(str, d[i])))
