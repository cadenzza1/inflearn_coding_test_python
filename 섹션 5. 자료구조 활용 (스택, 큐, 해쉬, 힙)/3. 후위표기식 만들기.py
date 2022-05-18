# +나 -를 만나면 스택의 모든 연산자들 pop하기!!
# 왜냐면 +(-)는 우선순위가 젤 낮고 스택에 먼저 들어가 있는 연산자들은
# +(-)보다 우선순위가 높거나 먼저 계산되어야 하는 친구들이기 때문이다
a=input()
stack = []
res = ''

for x in a:
    if x.isdecimal():
        res+=x
    else:
        if x=='(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x== '+' or x =='-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()

print(res)