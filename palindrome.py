x = 10
num = ''
num1 = x

if x < 0:
    print(False)

while x != 0:
    num += str(x % 10)
    x //= 10

print(num,x)