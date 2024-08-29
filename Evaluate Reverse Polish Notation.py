tokens = ["2","1","+","3","*"]
signs = {'*','/','+','-'}
stack = []
for token in tokens:
    if token in signs:
        one = stack.pop()
        two = stack.pop()
        stack.append(int(eval(f'{two} {token} {one}')))
    else:
        stack.append(token)

print(stack[0])
