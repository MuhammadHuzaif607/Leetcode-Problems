n = 8
for num in range(n//2 + 1):
    if num ** 2 == n:
        print(num)
        break
    elif num ** 2 > n:
        print(num-1)
        break


