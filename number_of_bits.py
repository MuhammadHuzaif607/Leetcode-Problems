n = 11
ones = 0
for bit in bin(n)[2:]:
    if bit == "1":
        ones += 1

print(ones)