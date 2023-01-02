# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(input().split())
n = int(input())


for i in range(n):
    other = set(input().split())
    if not A.issuperset(other):
        print(False)
        break
else:
    print(True)
