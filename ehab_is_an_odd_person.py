n = int(input())
num = list(map(int, input().split()))

ind = -1
odd = 0
even = 0
numb = sorted(num)

for i in range(len(numb)):
    if numb[i] % 2 != 0:
        odd +=1
        if even > 0:
            ind = i
            break
    elif numb[i] % 2 == 0:
        even +=1

    if odd > 0 and even > 0:
        ind = i
        break


if ind == -1:
    print(*num)
    
else:
    for i in range(ind, 0, -1):
        if numb[ind] < numb[i] and numb[ind] + numb[i] % 2!= 0:
            numb[i], numb[ind] = numb[ind], numb[i]
    print(*numb)
