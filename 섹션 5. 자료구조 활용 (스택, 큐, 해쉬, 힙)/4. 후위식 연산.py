a = input()
stack = []

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        b = stack.pop()
        a = stack.pop()
        if x == '+':
            stack.append(int(a)+int(b))
        if x == '-':
            stack.append(int(a)-int(b))
        if x == '*':
            stack.append(int(a)*int(b))
        if x == '/':
            stack.append(int(a)/int(b))

print(stack.pop())
