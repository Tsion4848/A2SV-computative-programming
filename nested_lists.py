if __name__ == '__main__':
    values = []
    only_sc = []
    dup_removed = []
    double_names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        values.append([name, score])
    
    for i in range(len(values)):
            only_sc.append(values[i][1])
    only_sc = sorted(only_sc)
    dup_removed = list(dict.fromkeys(only_sc))
    second = dup_removed[1]
    
    for i in range(len(values)):
        if values[i][1] == second:
            double_names.append(values[i][0])
    double_names = sorted(double_names)
    
    for name in double_names:
        print(name)
