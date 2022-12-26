class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        for i in num1:
            n1 = n1 * 10 + (ord(i) - 48)
            print(n1)
            
        for i in num2:
            n2 = n2 * 10 + (ord(i) - 48)
            print(n2)
            
        ans = n1 * n2
        
        print(str(ans))
        return str(ans)