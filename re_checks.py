import re

# integer_regex = r'^-?\d+$'
# string_regex = r'^[a-zA-z0-9]+$'
# float_regex = r'^-?\d\.(\d+)?$'


# test_strings = ['23213213213','hello1233213','-1',"3.","3.4"]

# for string in test_strings:
#     if re.match(string_regex,string):
#         print(f'{string} is of string type')
#     elif re.match(integer_regex,string):
#         print(f'{string} is of integer type')
#     elif re.match(float_regex,string):
#         print(f'{string} is of float type')
#     else:
#         print(f'{string} didn"t pass any type')

# For CNIC type

cnic_re = r"^\d{5}-\d{7}-\d{1}$"

print(re.match(cnic_re,"42101-6140357-9"))
