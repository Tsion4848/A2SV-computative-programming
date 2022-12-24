if __name__ == '__main__':
    N = int(input())
    inputs = []
    splitted = []
    answer = []
    for i in range(N):
        inputs.append((input()))
        
    for i in inputs:
        splitted.append(i.split())
        
    for i in range(len(splitted)):
        if (splitted[i][0] == 'insert'):
            answer.insert(int(splitted[i][1]),int(splitted[i][2]))
        elif (splitted[i][0] == 'remove'):
            answer.remove(int(splitted[i][1]))            
        elif (splitted[i][0] == 'append'):
            answer.append(int(splitted[i][1]))
        elif (splitted[i][0] == 'print'):
            print(answer)
        elif (splitted[i][0] == 'sort'):
            answer.sort()
        elif (splitted[i][0] == 'pop'):
            answer.pop()
        elif (splitted[i][0] == 'reverse'):
            answer.reverse()
        # answer = [int(j) for j in answer]
