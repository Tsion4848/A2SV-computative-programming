# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

k = int(input())

roomNo = map(int, input().split())

c = Counter(roomNo)

for key, val in c.items():
    if val != k:
        print(key)
        # print(keys[i])
