def swap_case(s):
    arr = ""
    for i in s:
        if i.islower():
            arr += i.capitalize()
        else:
            arr += i.lower()
    return arr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
