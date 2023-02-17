n, k = map(int, input().split())
num = list(map(int, input().split()))
num = sorted(num)

if k == n:
    print(num[k-1])
elif k == 0:
    if num[k] > 1:
        print(num[0] - 1)
    else:
        print(-1)
elif num[k] != num[k-1]:
    print(num[k-1])
else:
    print(-1)
