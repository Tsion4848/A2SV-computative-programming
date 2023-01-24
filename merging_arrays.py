inp= list(map(int, input().split()))
n = int(inp[0])
m = int(inp[1])

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

i = 0
j = 0

minim = min(n, m)
ans = []
while i < n and j < m:
    if list1[i] < list2[j]:
        # print(stlist1[i])
        ans.append(list1[i])
        i += 1
    else:
        # print(list2[j])
        ans.append(list2[j])
        j += 1

while i < n:
    # print(list1[i])
    ans.append(list1[i])
    i += 1

while j < m:
    # print(list2[j])
    ans.append(list2[j])
    j += 1

print(*ans)
