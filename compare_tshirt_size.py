for _ in range(int(input())):
    s1, s2 = map(str, input().strip().split())
    xs1 = s1.count('X')
    xs2 = s2.count('X')
    s1 = s1[::-1]
    s2 = s2[::-1]
    if s1[0] == 'S' and s2[0] == 'S':
        if xs1 > xs2:
            print('<')
        elif xs1 < xs2:
            print('>')
        else:
            print('=')
    elif s1[0] == 'L' and s2[0] == 'L':
        if xs1 > xs2:
            print('>')
        elif xs1 < xs2:
            print('<')
        else:
            print('=')

    elif (s1[0] == 'S' and (s2[0] == 'M' or s2[0] == 'L')):
        print('<')

    elif s1[0] == 'L' and (s2[0] == 'M' or s2[0] == 'S'):
        print('>')

    elif s1[0] == 'M':
        if s2[0] == 'S':
            print('>')
        elif s2[0] == 'L':
            print('<')
        elif s2[0] == 'M':
            print('=')
