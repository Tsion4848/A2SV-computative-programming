testc = int(input())
answer = []



for i in range(testc):
    numElements = int(input())
    arr = list(map(int, input().split()))
    pos = 0
    neg = float("-inf")
    first = 0
    ptr2 = 0
    summ = 0

    while ptr2 < len(arr) or first < len(arr):
        if arr[first] > 0:
            pos = arr[first]
            ptr2 = first + 1
            while ptr2 < len(arr):
                if arr[ptr2] > 0:
                    pos = max(pos, arr[ptr2])
                    ptr2 += 1
                else:
                    break

            summ += pos
            first = ptr2

        else:
            neg = arr[first]

            while ptr2 < len(arr):
                if arr[ptr2] < 0:
                    neg = max(neg, arr[ptr2])
                    ptr2 += 1
                else:
                    break
            summ += neg
            first = ptr2

    print(summ)
