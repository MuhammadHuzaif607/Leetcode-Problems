x = 64

def sqrt(x):
    lst = [i for i in range(1,(x//2)+1)]
    for num in lst[::-1]:
        if num ** 2 == x:
            return num

print(sqrt(x))