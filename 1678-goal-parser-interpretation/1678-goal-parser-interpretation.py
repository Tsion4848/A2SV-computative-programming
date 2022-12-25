class Solution:
    def interpret(self, command: str) -> str:
        answer = ""
        
        command = [*command]
        print(command)
        
        for i in range(len(command)):
            if command[i] == 'G':
                answer += "G"
            if command[i] == '(':
                if command[i+1] == ')':
                    answer += "o"
            if command[i] == ')':
                answer += ""
            if command[i] == '(' and command[i+1] == 'a' and command[i+2] == 'l' and command[i+3] == ')':
                answer += "al"
        return answer