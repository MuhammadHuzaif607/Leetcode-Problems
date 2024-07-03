num = 3949
rem = 0
mul = 0
str1 = ""

dict1 ={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

mul = num // 1000
num = num % 1000

str1 += mul * 'M'

if str(num)[0] == '9':
    mul = num // 900












