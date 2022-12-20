# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
words = []
coun = {}

for x in range(n):
    word = input()
    words.append(word)
    
    if word in coun:
        coun[word] += 1
    else:
        coun[word] = 1
        
print(len(coun))
for word in coun:
    print((coun[word]), end = ' ')
