num = 1994
values = {
    1:'I',
    5:'V',
    10:'X',
    50:'L',
    100:'C',
    500:'D',
    1000:'M'
}
roman = ''
th = num // 1000
num %= 1000
roman += th * values[1000]

nhundred = num // 900
num %= 900
roman += nhundred * 'CM'

fhundred = num // 500
num %= 500
roman += fhundred * values[500]


hundred = num // 100
num %= 100
if hundred == 4:
    roman += 'CD'
else:
    roman += hundred * values[100] 
    
    
ninety = num // 90
num %= 90
roman += ninety * 'XC'

fifty = num // 50
num %= 50

roman += fifty * values[50]

ten = num // 10
num %= 10

if ten == 4:
    roman += 'XL'
else:
    roman += ten * values[10]
    
nine = num // 9
num %= 9

roman += nine * 'IX'


five = num // 5
num %= 5

roman += five * values[5]

ones = num // 1
num %= 1

if ones == 4:
    roman += 'IV'
else:
    roman += ones * values[1]

print(roman,num)





