testC = int(input())

for _ in range(testC):
    flag = True
    num = int(input())
    inputt = list(set(map(int, input().split())))
    inputt = sorted(inputt)

    if len(inputt) == 1:
        print('YES')
        continue
    for i in range(len(inputt) - 1):
        if inputt[i+1] - inputt[i] <= 1:
            continue
        else:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
