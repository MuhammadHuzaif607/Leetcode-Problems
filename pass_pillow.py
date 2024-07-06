n = 18
time = 38

current = 1
direction = True

while time > 0:
    if direction:
        current += 1
    elif not direction:
        current -= 1

    if current == n:
        direction = False
        print('direction changed',n)
    elif current == 1 and not direction:
        direction = True
        
    time -= 1

print(current)

    