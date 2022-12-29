if __name__ == '__main__':
    n = int(input())
    arr = []
    answer = []
    for i in range(n):
        arr.append(input().split())
    # print(arr)

    for i in range(len(arr)):
        if (arr[i][0] == 'insert'):
            answer.insert(int(arr[i][1]),(arr[i][2]))
        elif (arr[i][0] == 'remove'):
            answer.remove(int(arr[i][1]))           
        elif (arr[i][0] == 'append'):
            answer.append(arr[i][1])
        elif (arr[i][0] == 'print'):
            print(answer)
        elif (arr[i][0] == 'sort'):
            answer.sort()
        elif (arr[i][0] == 'pop'):
            answer.pop()
        elif (arr[i][0] == 'reverse'):
            answer.reverse()
        answer = [int(j) for j in answer]
