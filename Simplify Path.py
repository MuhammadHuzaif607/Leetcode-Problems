path = "/home/"
directories = path.split("/")
print(directories)
stack = []

for directory in directories:
    if directory == ".." :
        if len(stack) == 0:
            continue
        else:
            stack.pop()
    elif directory == '' or directory == '.':
        continue
    else:
        print(directory)
        stack.append(directory)

s = '/'.join(stack)
s = '/' + s
print(s)