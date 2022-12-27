import textwrap

def wrap(string, max_width):
    str = ""
    n = 2
    for i in string:
        str += i
        if len(str) == max_width:
            str += '\n'
        if len(str) == (max_width * n) + (n-1):
            str += '\n'
            n += 1
    return str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
