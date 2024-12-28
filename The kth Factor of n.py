lst = []
n = 4
k = 4
lst.append(1)
for i in range(2,n//2 + 1):
    if n % i == 0:
        lst.append(i)

lst.append(n)
print(lst)
if len(lst) >= k -1:
    print(lst[k - 1])

    