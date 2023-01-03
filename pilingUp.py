# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    input()
    
    block = [int(x) for x in input().split()]
    minimum = block.index(min(block))
    
    left = block[:minimum]
    right = block[minimum+1:]
    
    if left == sorted(left, reverse = True) and right == sorted(right):
        print("Yes")
    else:
        print("No")
