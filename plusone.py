digits = [1]
num = ''
lst = []

for digit in digits:
    num += str(digit)
num = str(int(num) + 1)

for digit in num:
    lst.append(int(digit))

print(lst)

