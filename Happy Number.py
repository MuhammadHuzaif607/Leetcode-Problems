n = 19
def is_happy(n):
    mem = set()
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in mem:
            print(mem,n)
            return False
        else:
            mem.add(n)
    else:
        print(n)
        return True
        


print(is_happy(n))






        
