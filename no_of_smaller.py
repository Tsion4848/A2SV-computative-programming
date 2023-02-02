n, m = list(map(int, input().split()))

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

ptr1 = 0
less = []

for ptr2 in list2:
    while ptr1 < len(list1) and list1[ptr1] < ptr2:
        ptr1 += 1
    less.append(ptr1)
print(*less)
