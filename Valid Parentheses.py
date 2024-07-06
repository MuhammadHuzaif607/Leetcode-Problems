s = "(){}[]"
def isValid(s):
    dict1 = {
        ')': '(',
        '}':'{',
        ']':'['
    }
    closed_brackets = [')','}',']']
    stack = []
    for bracket in s:
        if bracket in closed_brackets:
            if len(stack) == 0:
                return False
            elif dict1[bracket] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)

    return True

print(isValid(s))
