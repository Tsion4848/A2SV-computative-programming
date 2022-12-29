# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input().split()   
nums = input().split();
A = set(input().split());
B = set(input().split());

happiness = 0
for i in nums:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1
print(happiness)
