if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    mylist = list(dict.fromkeys(arr))
    mylist = sorted(mylist)
    
    print(mylist[-2])
