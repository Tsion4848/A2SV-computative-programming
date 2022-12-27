# Enter your code here. Read input from STDIN. Print output to STDOUT

engNo = map(int, input())
engRollNo = set(map(int, input().split()))

frNo = map(int, input())
frRollNo = set(map(int, input().split()))

union = engRollNo | frRollNo
print(len(union))
