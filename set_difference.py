# Enter your code here. Read input from STDIN. Print output to STDOUT

english = map(int, input())
eng_rollno = set(map(int, input().split()))

french = map(int, input())
fr_rollno = set(map(int, input().split()))

only_eng = eng_rollno - fr_rollno

print(len(only_eng))

