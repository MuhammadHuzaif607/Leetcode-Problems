def compare(num1,num2):
    if num1 * num2 < 0:
        if abs(num1) > abs(num2):
            return num1
        elif abs(num1) < abs(num2):
            return num2
        else:
            return "Both will collide"
    return "No comparision"


asteroids = [8,-8]
len_ast = len(asteroids)
i = 1

while i < len_ast:
    val = compare(asteroids[-2],asteroids[-1])
    if val == "Both will collide":
        asteroids.pop(-1)
        asteroids.pop(-1)
        i += 2
    elif val == "No comparision":
        break
    else:
        asteroids.pop(-1)
        asteroids.pop(-1)
        asteroids.append(val)
    i += 1

print(asteroids)






